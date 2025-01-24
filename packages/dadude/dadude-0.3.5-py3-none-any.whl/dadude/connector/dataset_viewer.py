from enum import Enum
from dataclasses import dataclass
import duckdb

from dadude.config import DEFAULT_BUCKET, default_storage_config
from dadude.inspector import RemoteStorageClient


class DuckDbConncetionType(str, Enum):
    """
    Enum class for DuckDB connection type.
    """

    MEMORY = "memory"
    DISK = "disk"


remote = RemoteStorageClient(DEFAULT_BUCKET, default_storage_config)


@dataclass
class DatasetViewer:
    """
    Viewer class for a dataset.
    """

    name: str
    description: str
    remote_path: str
    remote: RemoteStorageClient = remote

    def __post_init__(self):
        self.remote_path = self.remote_path.strip("/")
        self.remote_path = f"{self.remote_path}/"
        self.duck = duckdb.connect(":memory:")
