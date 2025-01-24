from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from ydb_async.dialect import Dialect

def test_connection():
    engine = create_async_engine("sql+asyncydb://")
    assert isinstance(engine.dialect,  Dialect)
