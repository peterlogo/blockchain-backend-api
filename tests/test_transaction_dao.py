import pytest
from sqlmodel import SQLModel, create_engine, Session
from src.models.transaction_model import Transaction
from src.dao.transaction_dao import TransactionDAO
from tests.setup_db import setup_test_database

@pytest.fixture(scope="function")
def db_engine():
    engine = create_engine("sqlite:///:memory:", echo=False)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        setup_test_database(session, Transaction, 'transactions.json')
        yield session
    engine.dispose()

@pytest.mark.asyncio
async def test_get_all_transactions(db_engine):
    transaction_dao = TransactionDAO(db_engine)
    transactions = await transaction_dao.get_all_transactions()
    assert transactions is not None
    
@pytest.mark.asyncio
async def test_get_transaction_by_tx_hash(db_engine):
    tx_hash = '0xb4563fa94ba33'
    transaction_dao = TransactionDAO(db_engine)
    transaction = await transaction_dao.get_transaction_by_tx_hash(tx_hash)
    assert transaction is not None

@pytest.mark.asyncio
async def test_get_transaction_by_tx_hash_not_found(db_engine):
    tx_hash = '0xb4563fa94ba34'
    transaction_dao = TransactionDAO(db_engine)
    transaction = await transaction_dao.get_transaction_by_tx_hash(tx_hash)
    assert transaction is None
