import re

from sqlalchemy import MetaData, Table
from sqlalchemy.orm import declarative_base, relationship

# Base class for dynamically created models
Base = declarative_base()

apps_label = "datacubes"


class SqlAlchemyModelBuilder:
    _model_cache = {}  # Local cache for model classes

    def __init__(self, engine, table_name):
        """
        Initialize the model builder with a database engine and specific table.

        Args:
            engine: SQLAlchemy engine connected to the database.
            table_name (str): Name of the table to generate the model for.
        """
        self.engine = engine
        self.table_name = table_name
        self.metadata = MetaData()
        self.table = None  # Placeholder for the specific table
        self.class_name = self.normalize_class_name(self.table_name)

    def build_model(self) -> type:
        # Check if the model is already registered
        model = Base.registry._class_registry.get(self.class_name)
        if model:
            return model

        self.metadata.reflect(only=[self.table_name], bind=self.engine)
        self.table = self.metadata.tables.get(self.table_name)
        if self.table is None:
            raise ValueError(f"Table '{self.table_name}' does not exist in the database.")

        model = self.create_model()
        return model

    def create_model(self) -> type:
        """
        Create a SQLAlchemy ORM model for the reflected table.

        Returns:
            type: Dynamically generated SQLAlchemy ORM model class.
        """
        # Normalize the class name from the table name
        columns = self.get_columns(self.table)

        # Define attributes for the model class
        attrs = {
            "__tablename__": self.table_name,
            "__table__": self.table,
            "__module__": f"{apps_label}.models",
            "__mapper_args__": {"eager_defaults": True},
        }

        # Add columns and relationships to the model
        attrs.update(columns)
        # self.add_relationships(attrs, self.table)
        model = Base.registry._class_registry.get(self.class_name)
        if not model:
            model = type(self.class_name, (Base,), attrs)
            # Add the class to Base.registry so it is registered
            Base.registry._class_registry[self.class_name] = model
        return model

    def get_columns(self, table: Table):
        """
        Extract columns from the table and create corresponding SQLAlchemy fields.

        Args:
            table (Table): SQLAlchemy Table object.

        Returns:
            dict: Dictionary of column attributes.
        """
        columns = {}
        reserved_names = ["metadata", "class_", "table"]

        for column in table.columns:
            column_name = self.normalize_column_name(column.name)
            if column_name not in reserved_names:
                columns[column_name] = column
        return columns

    def add_relationships(self, attrs, table: Table):
        """
        Add relationships to the model for foreign keys.

        Args:
            attrs (dict): Attributes of the dynamically created model.
            table (Table): SQLAlchemy Table object.
        """
        for fk in table.foreign_keys:
            related_table_name = fk.column.table.name
            related_class_name = self.normalize_class_name(related_table_name)
            relationship_name = self.normalize_column_name(related_table_name)
            attrs[relationship_name] = relationship(related_class_name, back_populates=None)

    @staticmethod
    def normalize_class_name(table_name: str) -> str:
        """
        Normalize a table name into a valid Python class name.

        Args:
            table_name (str): Name of the table.

        Returns:
            str: Normalized class name.
        """
        return "".join(word.capitalize() for word in table_name.split("_"))

    @staticmethod
    def normalize_column_name(column_name: str) -> str:
        """
        Normalize a column name into a valid Python identifier.

        Args:
            column_name (str): Name of the column.

        Returns:
            str: Normalized column name.
        """
        column_name = re.sub(r"\W|^(?=\d)", "_", column_name)
        if column_name in {"class", "def", "return", "yield", "global"}:
            column_name += "_field"
        return column_name
