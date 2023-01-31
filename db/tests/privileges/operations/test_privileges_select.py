from db.metadata import get_empty_metadata
from db.privileges.operations.select import fetch_schema_privileges


def test_get_schema_privileges(engine_with_schema):
    engine, schema = engine_with_schema
    fetch_schema_privileges(engine, get_empty_metadata())
