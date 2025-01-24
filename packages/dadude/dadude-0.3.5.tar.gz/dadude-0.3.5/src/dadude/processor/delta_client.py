from enum import Enum

import pyarrow as pa
import pandas as pd
from deltalake import write_deltalake, DeltaTable

from dadude.config import (
    default_storage_config,
    DeltaStorageTier,
    DEFAULT_BUCKET,
    DEFAULT_LAKEHOUSE_PREFIX,
    # DEFAULT_CATALOG,
)
from dadude.log import logger


class DeltaWriterMode(str, Enum):
    OVERWRITE = "overwrite"
    APPEND = "append"
    IGNORE = "ignore"
    ERROR = "error"


class DeltaWriterSchemaMode(str, Enum):
    MERGE = "merge"
    OVERWRITE = "overwrite"


class DeltaReaderFormat(str, Enum):
    PANDAS = "pandas"
    PYARROW = "pyarrow"
    DELTA = "delta"


class DeltaClientError(Exception):
    """Base class for exceptions in this module."""

    pass


def read_delta_table(
    bucket: str,
    tier: str,
    table: str,
    version: int | None = None,
    preview: bool = False,
    format: DeltaReaderFormat = DeltaReaderFormat.PANDAS,
    local_cache_dir: str | None = None,
    storage_options: dict | None = default_storage_config,
) -> pd.DataFrame | pa.Table:
    tier_path = DeltaStorageTier(tier).value
    table_path = f"s3://{bucket}/{tier_path}/{table}"
    if version:
        logger.info(f"Reading {table} version {version}")
    else:
        logger.info(f"Reading latest version of {table} at {table_path}")
    try:
        dt = DeltaTable(
            table_path,
            version=version,
            storage_options=storage_options,
        )
    except Exception as e:
        logger.error(f"Error reading DeltaTable: {e}")
        raise DeltaClientError(f"Error reading DeltaTable: {e}")
    if format == "pandas":
        df_pdf = dt.to_pandas()
    else:
        df_pdf = dt.to_pyarrow_table()
    if preview:
        logger.info(f"Previewing first 5 rows of {table_path}")
        print(df_pdf.head())
    if local_cache_dir:
        logger.info(f"Saving DeltaTable to {local_cache_dir}")
        df_pdf.to_json(
            f"{local_cache_dir}/{table}.json", orient="records", lines=True, index=False
        )
    return df_pdf


def read_delta_table_from_catalog():
    raise NotImplementedError
    # return DeltaTable.from_data_catalog(
    #     data_catalog=DataCatalog.UNITY,
    #     database_name="materials",
    #     table_name="property_entity",
    # )


def read_delta_table_from_local():
    raise NotImplementedError


class DeltaWriter:
    def __init__(
        self,
        bucket: str = DEFAULT_BUCKET,
        prefix: str = DEFAULT_LAKEHOUSE_PREFIX,
        storage_options: dict = default_storage_config,
    ) -> None:
        self.storage_options = storage_options
        self.lakehouse_path = f"s3://{bucket}/{prefix}"

    def _write(
        self,
        resource_path: str,
        table: pd.DataFrame,
        mode: DeltaWriterMode = DeltaWriterMode.ERROR,
    ):
        # full_path = f"{self.bucket_path}/{resource_path}"
        logger.debug(f"Start: writing data to {resource_path}.")
        logger.warning(f"Mode: {mode}.")
        try:
            write_deltalake(
                resource_path,
                table,
                storage_options=self.storage_options,
                mode=mode,  # type: ignore
            )
            logger.info(f"Done: {resource_path=} written.")
        except Exception as e:
            logger.error(f"Error: {e}.")
            raise DeltaClientError(e)

    def _write_with_schema_mode(
        self,
        resource_path: str,
        table: pd.DataFrame,
        data_mode: DeltaWriterMode,
        schema_mode: DeltaWriterSchemaMode = DeltaWriterSchemaMode.MERGE,
    ):
        # TODO: this should not be a separate function
        logger.warning("Check: entering schema merge mode.")
        logger.debug(f"Start: writing data to {resource_path}.")
        logger.warning(f"Mode: {data_mode=}, {schema_mode=}.")
        try:
            write_deltalake(
                resource_path,
                table,
                storage_options=self.storage_options,
                mode=data_mode,  # type: ignore
                schema_mode=schema_mode,  # type: ignore
                engine="rust",
            )
        except Exception as e:
            logger.error(f"Error: {e}.")
            raise DeltaClientError(e)

    def write_json(
        self,
        json_file_path: str,
        lines=False,
        mode: DeltaWriterMode = DeltaWriterMode.ERROR,
        schema_mode: DeltaWriterSchemaMode | None = None,
    ):
        tier = DeltaStorageTier(json_file_path.split("/")[-2]).value
        table_name = json_file_path.split("/")[-1].split(".")[0].split("_v")[0]
        lake_path = f"{self.lakehouse_path}/{tier}/{table_name}/"
        # TODO: load json file into pyarrow table with schema inference
        # we use pd.DataFrame for now
        df = pd.read_json(json_file_path, lines=lines)
        logger.info(f"View: {df.head(1)}")
        if schema_mode is not None:
            self._write_with_schema_mode(lake_path, df, mode, schema_mode)
        else:
            self._write(lake_path, df, mode)
        logger.info(f"Done: {table_name=} written to {lake_path=}.")


def write_json_table(
    local_json_file_path: str,
    lines: bool = False,
    mode: DeltaWriterMode = DeltaWriterMode.ERROR,
):
    writer = DeltaWriter()
    writer.write_json(local_json_file_path, lines=lines, mode=mode)


def overwrite_json_table(
    local_json_file_path: str,
    lines: bool = False,
    mode: DeltaWriterMode = DeltaWriterMode.OVERWRITE,
):
    writer = DeltaWriter()
    writer.write_json(
        local_json_file_path,
        lines=lines,
        mode=mode,
        schema_mode=DeltaWriterSchemaMode.OVERWRITE,
    )


class DeltaClient:
    def __init__(
        self,
        bucket: str = DEFAULT_BUCKET,
        prefix: str = DEFAULT_LAKEHOUSE_PREFIX,
        storage_options: dict = default_storage_config,
    ):
        self.storage_options = storage_options
        self.location = f"s3a://{bucket}/{prefix}"

    def get_table_uri(
        self,
        tier: str,
        table: str,
        version: int | None = None,
        variant: str | None = None,
    ) -> str:
        if version is not None:
            return f"{self.location}/{tier}/{table}_v{version}_{variant}/"
        else:
            return f"{self.location}/{tier}/{table}_{variant}/"
