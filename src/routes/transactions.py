from typing import List
from fastapi import APIRouter, Depends, HTTPException
from src.models.transaction_model import Transaction
from src.dependencies.transaction_dependencies import get_transaction_service
from src.services.transaction_service import TransactionService

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
)

@router.get("/", response_model=List[Transaction])
async def get_transactions(transaction_service: TransactionService = Depends(get_transaction_service)):
    transactions = await transaction_service.get_all_transactions()
    if not transactions:
        raise HTTPException(status_code=404, detail="No transactions found")
    return transactions

@router.get("/{tx_hash}", response_model=Transaction)
async def get_transaction_by_hash(tx_hash: str, transaction_service: TransactionService = Depends(get_transaction_service)):
    transaction = await transaction_service.get_transaction_by_tx_hash(tx_hash)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction