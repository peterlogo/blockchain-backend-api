from src.dao.transaction_dao import TransactionDAO
from src.models.transaction_model import Transaction

class TransactionService:
    def __init__(self, transaction_dao: TransactionDAO):
        self.transaction_dao = transaction_dao
    
    def get_all_transactions(self) -> list[Transaction]:
        return self.transaction_dao.get_all_transactions()
    
    def get_transaction_by_tx_hash(self, tx_hash: str) -> Transaction:
        return self.transaction_dao.get_transaction_by_tx_hash(tx_hash)