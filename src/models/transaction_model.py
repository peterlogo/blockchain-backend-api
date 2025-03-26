from typing import Optional
from sqlmodel import SQLModel, Field

# Blockchain Transaction model for storing blockchain data in the database.
class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    from_address: str
    to_address: str
    amount: float
    timestamp: str
    tx_hash: str = Field(unique=True)