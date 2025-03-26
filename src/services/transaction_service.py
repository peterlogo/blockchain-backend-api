from src.dao.transaction_dao import TransactionDAO
from src.models.transaction_model import Transaction

class TransactionService:
    def __init__(self, transaction_dao: TransactionDAO):
        self.transaction_dao = transaction_dao
    
    async def create_transaction(self, transaction: Transaction) -> Transaction:
        return await self.transaction_dao.create_transaction(transaction)
    
    async def get_transaction_by_id(self, transaction_id: str) -> Transaction:
        return await self.transaction_dao.get_transaction_by_id(transaction_id)
    
    async def get_all_transactions(self) -> list[Transaction]:
        return await self.transaction_dao.get_all_transactions()
    
    async def get_transaction_by_tx_hash(self, tx_hash: str) -> Transaction:
        return await self.transaction_dao.get_transaction_by_tx_hash(tx_hash)