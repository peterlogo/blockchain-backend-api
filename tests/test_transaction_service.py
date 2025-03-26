import pytest
from unittest.mock import AsyncMock
from src.services.transaction_service import TransactionService
from src.dao.transaction_dao import TransactionDAO
from src.models.transaction_model import Transaction

def test_get_all_transactions():
    mock_dao = AsyncMock(TransactionDAO)
    mock_dao.get_all_transactions.return_value = [
        Transaction(id=1, from_address="address1", to_address="address2", amount=100, timestamp="2025-02-27T18:47:16.964967Z", tx_hash="0x1e8a2a258283c7"),
        Transaction(id=2, from_address="address3", to_address="address4", amount=200, timestamp="2025-02-27T18:47:16.964967Z", tx_hash="0x2e8a2a258283c7")
    ]

    service = TransactionService(mock_dao)
    transactions = service.get_all_transactions()
    assert len(transactions) == 2
    assert transactions[0].id == 1
    assert transactions[1].id == 2

def test_get_transaction_by_tx_hash():
    mock_dao = AsyncMock(TransactionDAO)
    mock_dao.get_transaction_by_tx_hash.return_value = Transaction(
        id=1, from_address="address1", to_address="address2", amount=100, timestamp="2025-02-27T18:47:16.964967Z", tx_hash="0x1e8a2a258283c7"
    )

    service = TransactionService(mock_dao)
    transaction = service.get_transaction_by_tx_hash("0x1e8a2a258283c7")
    assert transaction is not None
    assert transaction.tx_hash == "0x1e8a2a258283c7"

def test_get_transaction_not_found():
    mock_dao = AsyncMock(TransactionDAO)
    mock_dao.get_transaction_by_tx_hash.return_value = None
    service = TransactionService(mock_dao)
    transaction = service.get_transaction_by_tx_hash("0x1e8a2a258283c9")
    assert transaction is None