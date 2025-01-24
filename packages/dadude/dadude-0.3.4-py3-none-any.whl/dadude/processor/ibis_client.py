from enum import Enum
from pathlib import Path

import ibis
import ibis.backends
import pandas as pd
import pyarrow as pa

from dadude.config import default_storage_config
from dadude.log import logger


IbisSourceRepr = str | Path | pa.Table | pd.DataFrame


class IbisIntegratedBackend(str, Enum):
    DUCKDB = "duckdb"
    PYSPARK = "pyspark"


class IbisReaderMode(str, Enum):
    TABLE = "table"
    DATAFRAME = "dataframe"


class IbisReader:
    """
    A read-only client for accessing data in a lakehouse locally via Ibis dataframe frontend.
    """

    def __init__(
        self,
        backend: IbisIntegratedBackend = IbisIntegratedBackend.DUCKDB,
        storage_config: dict | None = default_storage_config,
        local_db_path: str | None = None,
        read_only: bool = False,
        num_threads: int = 1,
        memory_limit: str = "1GB",
        interactive: bool = False,
    ):
        self.logger = logger
        self.backend = backend
        self.storage_config = storage_config
        conn_str = f"{self.backend.value}://{local_db_path or ":memory:"}"
        self.logger.debug(f"Connecting to {conn_str}")
        self.conn = ibis.connect(
            conn_str,
            read_only=read_only,
            threads=num_threads,
            memory_limit=memory_limit,
        )
        ibis.options.interactive = interactive

    def list_tables(self):
        """List all tables in the current database."""
        return self.conn.list_tables()

    def list_catalogs(self):
        """List all available catalogs in the database."""
        return self.conn.list_catalogs()  # type: ignore

    def list_databases(self):
        """List all available databases."""
        return self.conn.list_databases()  # type: ignore

    def read_delta_table(
        self,
        table_path: str,
        mode: IbisReaderMode = IbisReaderMode.TABLE,
    ) -> pa.Table | pd.DataFrame:
        """
        Read a Delta Lake table from the specified (remote) path.

        Args:
            table_path: Path to the Delta Lake table
            mode: Output format (TABLE for PyArrow Table, DATAFRAME for pandas DataFrame)

        Returns:
            PyArrow Table or pandas DataFrame depending on mode
        """
        delta_table = ibis.read_delta(
            table_path,
            storage_options=self.storage_config,
        )
        match mode:
            case IbisReaderMode.TABLE:
                return delta_table.to_pyarrow()
            case IbisReaderMode.DATAFRAME:
                return delta_table.to_pandas()

    def write_table(self, table_name: str, path: str):
        """Write table to specified path (Not implemented in reader)."""
        raise NotImplementedError("Not implemented in reader.")

    def create_table(
        self,
        table_name: str,
        obj: pa.Table | pd.DataFrame,
        overwrite: bool = False,
        schema: ibis.Schema | None = None,  # type: ignore
    ):
        """
        Create a new table using an object in memory to the connected database.

        Args:
            table_name: Name of the table to create
            obj: PyArrow Table or pandas DataFrame to create table from
            overwrite: If True, overwrites existing table
            schema: Optional schema definition for the table
        """
        self.conn.create_table(table_name, obj, overwrite=overwrite, schema=schema)

    def get_table(self, table_name: str) -> ibis.Table:
        """Get an `ibis.Table` object for the specified table name."""
        return self.conn.table(table_name)

    def get_table_schema(self, table_name: str) -> ibis.Schema:
        """Get the schema of the specified table."""
        return self.conn.get_schema(table_name)  # type: ignore

    def get_table_columns(self, table_name: str) -> list[str]:
        """Get list of column names for the specified table."""
        return self.conn.table(table_name).columns

    def register_table(self, file_path: IbisSourceRepr, table_name: str):
        """
        Register an external data source as a table.

        Args:
            file_path: Path or data object to register
            table_name: Name to register the table as
        """
        self.conn.register(file_path, table_name)  # type: ignore

    def rename_table(self, old_table_name: str, new_table_name: str):
        """Rename a table from old_table_name to new_table_name."""
        self.conn.rename_table(old_table_name, new_table_name)

    def insert_to(
        self,
        table_name: str,
        obj: pd.DataFrame | ibis.Table | list | dict,
        overwrite: bool = False,
    ):
        """
        Insert data into an existing table.

        Args:
            table_name: Target table name
            obj: Data to insert (DataFrame, Ibis Table, list, or dict)
            overwrite: If True, overwrites existing data
        """
        self.conn.insert(table_name, obj, overwrite=overwrite)  # type: ignore

    def drop_table(self, table_name: str):
        """Drop (delete) the specified table from the database."""
        self.conn.drop_table(table_name)
        self.logger.info(f"Dropped table {table_name}")


if __name__ == "__main__":
    reader = IbisReader(
        local_db_path="db/test.db",
        read_only=True,
        num_threads=4,
        memory_limit="1GB",
    )
    print(reader.list_tables())
