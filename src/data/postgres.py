from sqlmodel import create_engine, Session
from src.config import Config

config = Config()
engine = create_engine(config.DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session