import os
from enum import Enum
from dotenv import load_dotenv

from deltalake.data_catalog import DataCatalog


load_dotenv()


DEFAULT_CATALOG = DataCatalog.UNITY
DEFAULT_BUCKET = os.getenv("STORAGE_BUCKET", "")
DEFAULT_LAKEHOUSE_PREFIX = "materials/lakehouse"


default_storage_config = {
    "AWS_ACCESS_KEY_ID": os.getenv("STORAGE_ACCESS_KEY_ID", ""),
    "AWS_SECRET_ACCESS_KEY": os.getenv("STORAGE_SECRET_ACCESS_KEY", ""),
    "AWS_ENDPOINT_URL": os.getenv("STORAGE_ENDPOINT_URL", ""),
    "AWS_REGION": os.getenv("STORAGE_REGION", ""),
    "AWS_S3_ALLOW_UNSAFE_RENAME": "true",
    "AWS_ALLOW_HTTP": "true",
}


class DeltaStorageTier(str, Enum):
    BRONZE = "bronze"
    SILVER = "silver"
    GOLD = "gold"
    INBOX = "inbox"
    STAGING = "staging"
    VIEW = "view"
    TEST = "test"
