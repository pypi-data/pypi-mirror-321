import datetime
from concurrent.futures import ThreadPoolExecutor
from typing import Type, Any, Dict, Optional

import fsspec
import pandas as pd
from IPython.display import display
from tqdm import tqdm

from sibi_dst.utils import Logger
from sibi_dst.utils import ParquetSaver


class DataWrapper:
    DEFAULT_MAX_AGE_MINUTES = 1440
    DEFAULT_HISTORY_DAYS_THRESHOLD = 30

    def __init__(self,
                 dataclass: Type,
                 date_field: str,
                 data_path: str,
                 parquet_filename: str,
                 start_date: Any,
                 end_date: Any,
                 fs: Optional[fsspec.AbstractFileSystem] = None,
                 filesystem_type: str = "file",
                 filesystem_options: Optional[Dict] = None,
                 verbose: bool = False,
                 class_params: Optional[Dict] = None,
                 load_params: Optional[Dict] = None,
                 reverse_order: bool = False,
                 overwrite: bool = False,
                 ignore_missing: bool = False,
                 logger: Optional[Logger] = None,
                 max_age_minutes: int = DEFAULT_MAX_AGE_MINUTES,
                 history_days_threshold: int = DEFAULT_HISTORY_DAYS_THRESHOLD,
                 show_progress: bool = False,
                 timeout: Optional[int] = 300):
        self.dataclass = dataclass
        self.date_field = date_field
        self.data_path = self.ensure_forward_slash(data_path)
        self.parquet_filename = parquet_filename
        self.filesystem_type = filesystem_type
        self.filesystem_options = filesystem_options or {}
        self.fs = fs or fsspec.filesystem(filesystem_type, **self.filesystem_options)
        self.verbose = verbose
        self.class_params = class_params or {}
        self.load_params = load_params or {}
        self.reverse_order = reverse_order
        self.overwrite = overwrite
        self.ignore_missing = ignore_missing
        self.logger = logger or Logger.default_logger(logger_name=self.dataclass.__name__)
        self.max_age_minutes = max_age_minutes
        self.history_days_threshold = history_days_threshold
        self.show_progress = show_progress
        self.timeout = timeout

        self.start_date = self.convert_to_date(start_date)
        self.end_date = self.convert_to_date(end_date)

    @staticmethod
    def convert_to_date(date: Any) -> datetime.date:
        if isinstance(date, datetime.date):
            return date
        try:
            return pd.to_datetime(date).date()
        except ValueError as e:
            raise ValueError(f"Error converting {date} to datetime: {e}")

    @staticmethod
    def ensure_forward_slash(path: str) -> str:
        return path if path.endswith('/') else path + '/'

    def generate_date_range(self):
        """Generate a range of dates between start_date and end_date."""
        date_range = pd.date_range(self.start_date, self.end_date, freq='D')
        if self.reverse_order:
            date_range = date_range[::-1]
        for date in date_range:
            yield date.date()

    def process(self):
        """Execute the update plan using 'update_priority' to determine processing order."""
        update_plan_table = self.generate_update_plan_with_conditions()

        # Display the update plan table to the user if requested
        if self.show_progress:
            display(update_plan_table)

        # Filter out rows that do not require updates (priority 0 means skip)
        update_plan_table = update_plan_table[
            (update_plan_table["update_required"] == True) & (update_plan_table["update_priority"] != 0)
            ]

        # Group by priority
        priorities = sorted(update_plan_table["update_priority"].unique())

        # We will process each priority level in its own thread.
        # Each thread will handle all dates associated with that priority.
        def process_priority(priority):
            # Extract dates for the current priority
            dates_to_process = update_plan_table[
                update_plan_table["update_priority"] == priority
                ]["date"].tolist()

            # If show_progress is True, wrap in a progress bar
            date_iterator = dates_to_process
            if self.show_progress:
                date_iterator = tqdm(date_iterator, desc=f"Processing priority {priority}:{self.dataclass.__name__}",
                                     unit="date")

            # Process each date for this priority
            for current_date in date_iterator:
                self.process_date(current_date)

        # Launch a separate thread for each priority
        with ThreadPoolExecutor(max_workers=len(priorities)) as executor:
            futures = {executor.submit(process_priority, p): p for p in priorities}
            for future in futures:
                try:
                    future.result(timeout=self.timeout)
                except TimeoutError:
                    self.logger.error(f"Thread for {self.dataclass.__name__} timed out. Thread cancelled.")
                    future.cancel()
                    priority = futures[future]
                    new_future = executor.submit(process_priority, priority)
                    futures[new_future] = priority
                    self.logger.info(f"Resubmitted task for priority {priority} after timeout.")

    def is_file_older_than(self, file_path: str) -> bool:
        """
        Check if a file is older than the specified max_age_minutes.

        :param file_path: Path to the file.
        :return: True if the file is older than max_age_minutes, False otherwise.
        """
        try:
            # Get file info
            info = self.fs.info(file_path)

            # Determine the modification time from available keys
            file_modification_time = None
            if "mtime" in info:  # Local filesystem
                file_modification_time = info["mtime"]
                file_modification_datetime = datetime.datetime.fromtimestamp(
                    file_modification_time, tz=datetime.timezone.utc
                )
            elif "LastModified" in info:  # S3-compatible filesystem
                file_modification_datetime = (
                    info["LastModified"] if isinstance(info["LastModified"], datetime.datetime)
                    else datetime.datetime.strptime(info["LastModified"], "%Y-%m-%dT%H:%M:%S.%fZ")
                )
            else:
                self.logger.warning(f"Modification time not available for {file_path}.")
                return True  # Assume file is too old if we cannot determine its age

            # Compare file age
            current_time = datetime.datetime.now(datetime.timezone.utc)
            file_age_minutes = (current_time - file_modification_datetime).total_seconds() / 60
            self.logger.info(
                f"File {file_path} is {round(file_age_minutes, 2)} minutes old "
                f"(threshold: {self.max_age_minutes} minutes)"
            )
            return file_age_minutes > self.max_age_minutes

        except FileNotFoundError:
            self.logger.warning(f"File {file_path} not found.")
            return True  # File is considered old if it doesn't exist
        except Exception as e:
            self.logger.error(f"Error checking file age for {file_path}: {str(e)}")
            return True  #

    def process_date(self, date: datetime.date):
        """Process a specific date by regenerating data as necessary."""
        folder = f'{self.data_path}{date.year}/{date.month:02d}/{date.day:02d}/'
        full_parquet_filename = f"{folder}{self.parquet_filename}"

        start_time = datetime.datetime.now()
        self.logger.info(f"Processing {full_parquet_filename}...")

        data_object = self.dataclass(**self.class_params)
        df = data_object.load_period(dt_field=self.date_field, start=date, end=date)

        if len(df.index) == 0:
            self.logger.error("No data found for the specified date.")
            return

        parquet_saver = ParquetSaver(df, parquet_storage_path=folder, logger=self.logger, fs=self.fs)
        parquet_saver.save_to_parquet(self.parquet_filename, clear_existing=True)

        end_time = datetime.datetime.now()
        duration_seconds = (end_time - start_time).total_seconds()
        self.logger.info(
            f"Data saved to {full_parquet_filename}. Processing time: {duration_seconds:.2f} seconds"
        )

    def generate_update_plan_with_conditions(self):
        """
        Generate an update plan that evaluates files based on the specified hierarchy:
        1. Overwrite (all files regenerated).
        2. History threshold: Files within `history_days_threshold` are evaluated for `max_age_minutes`.
        3. Missing files: Detect missing files, ignoring future dates.
        """
        rows = []

        today = datetime.date.today()
        history_start_date = today - datetime.timedelta(days=self.history_days_threshold)

        date_range = self.generate_date_range()
        if self.show_progress:
            date_range = tqdm(date_range, desc=f"Evaluating update plan:{self.dataclass.__name__}", unit="date")

        for current_date in date_range:
            folder = f'{self.data_path}{current_date.year}/{current_date.month:02d}/{current_date.day:02d}/'
            full_parquet_filename = f"{folder}{self.parquet_filename}"

            file_exists = self.fs.exists(full_parquet_filename)
            within_history = history_start_date <= current_date <= today
            missing_file = not file_exists and not self.ignore_missing
            category = None

            # Hierarchy 1: Overwrite
            if self.overwrite:
                category = "overwrite"
                update_required = True
            # Hierarchy 2: History threshold evaluation
            elif within_history:
                if self.is_file_older_than(full_parquet_filename):
                    category = "history_days"
                    update_required = True
                else:
                    category = "file age is recent"
                    update_required = False
            # Hierarchy 3: Missing files
            elif missing_file and current_date <= today:
                category = "missing_files"
                update_required = True
            else:
                category = "No Update Required"
                update_required = False

            # Collect condition descriptions for the update plan table
            rows.append({
                "date": current_date,
                "file_exists": file_exists,
                "within_history": within_history,
                "missing_file": missing_file,
                "update_required": update_required,
                "update_category": category,
                "datawrapper class": self.dataclass.__name__
            })
            priority_map = {
                "overwrite": 1,
                "history_days": 2,
                "missing_files": 3
            }

            for row in rows:
                category = row.get("update_category")
                # Default to None if no category assigned (no update required)
                row["update_priority"] = priority_map.get(category, 0)

        update_plan_table = pd.DataFrame(rows)
        return update_plan_table

# # wrapper.process()
# # wrapper = DataWrapper(
# #    dataclass=YourDataClass,
# #    date_field="created_at",
# #    data_path="s3://your-bucket-name/path/to/data",
# #    parquet_filename="data.parquet",
# #    start_date="2022-01-01",
# #    end_date="2022-12-31",
# #    filesystem_type="s3",
# #    filesystem_options={
# #        "key": "your_aws_access_key",
# #        "secret": "your_aws_secret_key",
# #        "client_kwargs": {"endpoint_url": "https://s3.amazonaws.com"}
# #    },
# #    verbose=True
# #)
# #wrapper.process()
