from fastapi import Depends
from sqlmodel import Session
from src.data.postgres import get_session
from src.dao.transaction_dao import TransactionDAO
from src.services.transaction_service import TransactionService

def get_transaction_dao(session: Session = Depends(get_session)):
    return TransactionDAO(session)

def get_transaction_service(transaction_dao: TransactionDAO = Depends(get_transaction_dao)):
    return TransactionService(transaction_dao)