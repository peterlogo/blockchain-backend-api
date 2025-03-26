import os
import json
import logging
from sqlmodel import SQLModel, Session, select
from .postgres import engine
from src.models.transaction_model import Transaction

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

async def initialize_db():
    try:
        SQLModel.metadata.create_all(engine)
        logger.info("Database initialized successfully.")
    except Exception as e:
        logger.error(f"Failed to initialize database: {str(e)}")
        return
    
    try:
        with Session(engine) as session:
            statement = select(Transaction)
            result = session.exec(statement).all()
            if not result:
                file_path = os.path.join(os.path.dirname(__file__), "transactions.json")
                if os.path.exists(file_path):
                    with open(file_path, "r") as file:
                        transactions = json.load(file)
                        if transactions is None:
                            logger.warning("No transactions found in JSON file.")
                            return
                        for transaction in transactions:
                            transaction_obj = Transaction(**transaction)
                            session.add(transaction_obj)
                            session.commit()
                        logger.info("Transactions loaded from JSON file successfully.")
                else:
                    logger.warning("No transactions found in JSON file.")
            else:
                logger.info("Transactions already loaded in the database.")
    except Exception as e:
        logger.error(f"Failed to load transactions from JSON file: {str(e)}")