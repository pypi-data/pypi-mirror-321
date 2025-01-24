import pytest
from dadude.processor.ibis_client import IbisReader


@pytest.fixture
def db_writer():
    return IbisReader().conn


def test_list_tables(db_writer):
    assert db_writer.list_tables() == []
