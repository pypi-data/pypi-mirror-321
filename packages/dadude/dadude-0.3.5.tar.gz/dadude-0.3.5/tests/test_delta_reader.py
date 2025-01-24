import pytest
import pandas as pd
from dadude.processor.delta_client import read_delta_table


@pytest.fixture
def qa_table_path():
    return "material_property_entity_v3/"


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


def test_read_delta_table(qa_table_path, storage_options):
    df = read_delta_table(
        "matter-most", "gold", qa_table_path, storage_options=storage_options
    )
    assert isinstance(df, pd.DataFrame)
    assert set(df.columns) == {
        "ppi_id",
        "class_ii_name",
        "print_friendly_units",
        "statistical_type",
        "upper_bound",
        "class_i_name",
        "lower_bound",
        "created_at",
        "display_name_en",
        "application_domain",
        "domain_id",
        "domain_name_cn",
        "parent_ppi_id",
        "alias_list_en",
        "class_iii_name",
        "updated_at",
        "display_name_cn",
        "unit_recognition",
        "alias_list_cn",
    }
    assert len(df) == 1383
