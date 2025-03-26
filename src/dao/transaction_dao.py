import logging
from sqlmodel import Session, select
from models.transaction_model import Transaction

logger = logging.getLogger(__name__)

class TransactionDAO:
    def __init__(self, session: Session):
        self.session = session
    
    async def create_transaction(self, transaction: Transaction) -> Transaction:
        try:
            await self.session.add(transaction)
            await self.session.commit()
            return transaction
        except Exception as e:
            logger.error(f"Error creating transaction: {e}")
            await self.session.rollback()
            raise e
        
    async def get_transaction_by_id(self, transaction_id: int) -> Transaction:
        try:
            transaction = await self.session.fetch_one(select(Transaction).where(Transaction.id == transaction_id))
            return transaction
        except Exception as e:
            logger.error(f"Error fetching transaction by ID: {e}")
            raise e
        
    async def get_all_transactions(self) -> list[Transaction]:
        try:
            transactions = await self.session.fetch_all(select(Transaction))
            return transactions
        except Exception as e:
            logger.error(f"Error fetching all transactions: {e}")
            raise e
    
    async def get_transaction_by_tx_hash(self, tx_hash: str) -> Transaction:
        try:
            transaction = await self.session.fetch_one(select(Transaction).where(Transaction.tx_hash == tx_hash))
            return transaction
        except Exception as e:
            logger.error(f"Error fetching transaction by tx_hash: {e}")
            raise e