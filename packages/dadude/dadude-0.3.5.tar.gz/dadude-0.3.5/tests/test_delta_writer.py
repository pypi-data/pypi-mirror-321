import pytest
import pyarrow as pa

from dadude.processor.delta_client import (
    DeltaWriter,
    DeltaReaderFormat,
    read_delta_table,
)


@pytest.fixture
def storage_options():
    return {
        "AWS_ACCESS_KEY_ID": "iamdev",
        "AWS_SECRET_ACCESS_KEY": "xzd19950506",
        "AWS_ENDPOINT_URL": "http://192.168.18.206:9000",
        "AWS_REGION": "us-east-1",
        "AWS_S3_ALLOW_UNSAFE_RENAME": "true",
        "AWS_ALLOW_HTTP": "true",
    }


@pytest.fixture
def bucket():
    return "matter-most"


def test_delta_writer(storage_options, bucket):
    # write some data into a delta table
    df = pa.table({"id": [1, 2], "value": ["foo", "bar"]})
    writer = DeltaWriter(bucket, storage_options=storage_options)
    writer._write("test/pyarrow_table/", df)
    table = read_delta_table(
        bucket,
        "test",
        "pyarrow_table/",
        format=DeltaReaderFormat.PYARROW,
        storage_options=storage_options,
    )
    assert table.equals(df)
