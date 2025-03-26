import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    return TestClient(app)


@pytest.mark.asyncio
async def test_get_all_transactions(client):
    response = client.get("/transactions")
    transactions = response.json()

    assert response.status_code == 200
    assert len(transactions) > 0


@pytest.mark.asyncio
async def test_get_transaction_by_tx_hash(client):
    response = client.get("/transactions/0xb4563fa94ba33")
    transaction = response.json()
    assert response.status_code == 200
    assert transaction["tx_hash"] == "0xb4563fa94ba33"

@pytest.mark.asyncio
async def test_get_transaction_by_invalid_tx_hash(client):
    response = client.get("/transactions/invalid_tx_hash")
    assert response.status_code == 404
    assert response.json()["detail"] == "Transaction not found"