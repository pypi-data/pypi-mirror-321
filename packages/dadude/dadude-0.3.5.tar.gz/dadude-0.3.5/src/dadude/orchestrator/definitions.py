from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    load_assets_from_modules,
)

from dagster_deltalake import S3Config
from dagster_deltalake.config import ClientConfig
from dagster_deltalake_pandas import DeltaLakePandasIOManager

from dadude.config import default_storage_config, DEFAULT_BUCKET
from dadude.orchestrator import assets

all_assets = load_assets_from_modules([assets])

default_s3_config = S3Config(
    access_key_id=default_storage_config["AWS_ACCESS_KEY_ID"],
    secret_access_key=default_storage_config["AWS_SECRET_ACCESS_KEY"],
    endpoint=default_storage_config["AWS_ENDPOINT_URL"],
    region=default_storage_config["AWS_REGION"],
    bucket=DEFAULT_BUCKET,
    allow_unsafe_rename=True,
)


entity_update_schedule = ScheduleDefinition(
    name="entity_update_schedule",
    target=AssetSelection.all(),
    cron_schedule="0 0 * * 6",  # Every Saturday
)

defs = Definitions(
    assets=all_assets,
    resources={
        "io_manager": DeltaLakePandasIOManager(
            root_uri=f"s3://{DEFAULT_BUCKET}/materials/lakehouse/test/",
            storage_options=default_s3_config,
            client_options=ClientConfig(allow_http=True),
            schema="dagster_dev",
        )
    },
    schedules=[entity_update_schedule],
)
