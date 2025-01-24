import pytest
from dadude.inspector import RemoteStorageClient


@pytest.fixture
def self_hosted_minio_client():
    minio_config = {
        "AWS_ACCESS_KEY_ID": "iamdev",
        "AWS_SECRET_ACCESS_KEY": "xzd19950506",
        "AWS_ENDPOINT_URL": "http://192.168.18.206:9000",
        "AWS_REGION": "us-east-1",
    }
    my_client = RemoteStorageClient("matter-most", minio_config)
    return my_client


@pytest.fixture
def ops_ceph_client():
    ops_ceph_config = {
        "AWS_ACCESS_KEY_ID": "k2W8hPYxUP5NTbFB",
        "AWS_SECRET_ACCESS_KEY": "icrIfxbLNv8gtURdRkFJH3lbIWMSixDT",
        "AWS_ENDPOINT_URL": "http://local-minio-s3-api.patsnap.io",
        "AWS_REGION": "us-east-1",
    }
    ops_client = RemoteStorageClient("local-rd-common/matter-most", ops_ceph_config)
    return ops_client


def test_minio_list_resource(self_hosted_minio_client):
    resources = self_hosted_minio_client._list_resource_files(
        "gold/material_property_entity_v3"
    )
    assert len(resources) == 2


def test_minio_list_sub_directory(self_hosted_minio_client):
    sub_dirs = self_hosted_minio_client._list_sub_directory("")
    assert len(sub_dirs) == 6
    assert sub_dirs[0] == "bronze"
