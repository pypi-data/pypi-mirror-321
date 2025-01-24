from dataclasses import dataclass
import boto3

from dadude.config import DEFAULT_BUCKET, default_storage_config
from dadude.log import logger


# TODO: Why did I re-implement this module here from `pyrogen`?


@dataclass
class S3RemoteObject:
    name: str
    last_modified_date: str
    last_modified_time: str
    size: int
    storage_class: str = "STANDARD"
    prefix: str = ""

    @classmethod
    def from_response(cls, s3_response: dict, prefix):
        return cls(
            s3_response["Key"],
            s3_response["LastModified"].strftime("%Y-%m-%d"),
            s3_response["LastModified"].strftime("%H:%M:%S"),
            s3_response["Size"],
            s3_response["StorageClass"],
            prefix,
        )

    @staticmethod
    def parse_size_unit(size):
        if size < 1024:
            return str(size) + "B"
        elif size < 1024**2:
            return str(size // 1024) + "KB"
        elif size < 1024**3:
            return str(size // 1024**2) + "MB"
        else:
            return str(size // 1024**3) + "GB"

    def __str__(self):
        return "\t".join(
            (
                self.last_modified_date,
                self.last_modified_time,
                self.parse_size_unit(self.size),
                self.name[len(self.prefix) :],
            )
        )


class RemoteStorageClient:
    """
    The access entry to a remote storage.
    It is used to access all the other resources in the remote object storage, except for the lakehouse.
    """

    def __init__(self, bucket_path: str, storage_config: dict) -> None:
        self.logger = logger
        self.root = bucket_path
        self.default_dataset_prefix = "materials/datasets/"
        self.default_model_prefix = "materials/models/"
        self.default_evaluation_prefix = "materials/evaluations/"
        self.logger.debug("Connecting to S3...")
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=storage_config["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=storage_config["AWS_SECRET_ACCESS_KEY"],
            endpoint_url=storage_config["AWS_ENDPOINT_URL"],
            region_name=storage_config["AWS_REGION"],
        )
        self.logger.debug("Connected to S3 successfully.")

    def _list_sub_directory(self, prefix) -> list[str]:
        self.logger.info(f"Listing {self.root}/{prefix} in the remote directory...")
        all_objects = self.s3.list_objects_v2(
            Bucket=self.root,
            Delimiter="/",
            Prefix=prefix,
        )["CommonPrefixes"]
        return [
            dir_path["Prefix"][len(prefix) : -1]
            for dir_path in all_objects
            if dir_path["Prefix"].startswith(prefix)
        ]

    def list_datasets(self) -> list[str]:
        return self._list_sub_directory(self.default_dataset_prefix)

    def list_models(self) -> list[str]:
        return self._list_sub_directory(self.default_model_prefix)

    def list_evaluations(self) -> list[str]:
        return self._list_sub_directory(self.default_evaluation_prefix)

    def _list_resource_files(self, prefix, subpath="") -> list[str]:
        prefix += subpath
        if not prefix.endswith("/"):
            logger.warning(f"Appending '/' to the prefix {prefix}...")
            prefix += "/"
        logger.info(f"{self.root=}, {prefix=}")
        all_objects = self.s3.list_objects_v2(
            Bucket=self.root, Delimiter="/", Prefix=prefix
        )["Contents"]
        # TODO: handle the sub directory objects
        resouce_rows = []
        resouce_column_headers = "\t".join(["MOD_DATE", "MOD_TIME", "SIZE", "NAME"])
        resouce_rows.append(resouce_column_headers)
        for obj in all_objects:
            resouce_rows.append(str(S3RemoteObject.from_response(obj, prefix)))
        return resouce_rows

    def list_dataset_files(self, dataset_name) -> list[str]:
        return self._list_resource_files(self.default_dataset_prefix, dataset_name)

    def list_model_files(self, model_name) -> list[str]:
        return self._list_resource_files(self.default_model_prefix, model_name)

    def list_evaluation_files(self, eval_name) -> list[str]:
        return self._list_resource_files(self.default_evaluation_prefix, eval_name)

    def download_model_from_huggingface(self, model_name, local_paths):
        # TODO: implement this via Huggingface API
        raise NotImplementedError

    def download_file_from_remote_to_local(self, key, local_path):
        # TODO: implement this via CBS
        raise NotImplementedError

    def upload_file_from_local_to_remote(self, key, local_path):
        # TODO: implement this via CBS
        raise NotImplementedError

    def move_file_from_remote_to_another(self, key, new_key):
        # TODO: implement this via CBS
        raise NotImplementedError


if __name__ == "__main__":
    remote_storage = RemoteStorageClient(DEFAULT_BUCKET, default_storage_config)
    print("\n".join(remote_storage.list_models()))
    print("\n".join(remote_storage._list_resource_files("materials/packages/")))
