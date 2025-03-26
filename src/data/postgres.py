from sqlmodel import create_engine, Session

DATABASE_URL = "postgresql://postgres:password@localhost:5432/mydatabase"
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session