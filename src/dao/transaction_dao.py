import logging
from sqlmodel import select, Session
from src.models.transaction_model import Transaction

logger = logging.getLogger(__name__)

class TransactionDAO:
    def __init__(self, session: Session):
        self.session = session
        
    def get_all_transactions(self) -> list[Transaction]:
        try:
            statement = select(Transaction)
            transactions = self.session.exec(statement)
            return transactions.all()
        except Exception as e:
            logger.error(f"Error fetching all transactions: {e}")
            raise e
    
    def get_transaction_by_tx_hash(self, tx_hash: str) -> Transaction:
        try:
            statement = select(Transaction).where(Transaction.tx_hash == tx_hash)
            transaction = self.session.exec(statement)
            return transaction.first()
        except Exception as e:
            logger.error(f"Error fetching transaction by tx_hash: {e}")
            raise e