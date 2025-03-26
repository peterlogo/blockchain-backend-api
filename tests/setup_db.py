import os
import logging
import json
from sqlmodel import Session, SQLModel, select

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
def setup_test_database(session: Session, model: SQLModel, file: str) -> None:
    """
    Set up a test database by loading data from a JSON file if the database is empty.

    This function checks if the specified database table is empty. If it is, it attempts to load data
    from a JSON file and populate the database. If the table already contains data, it logs a message
    indicating that the data is already loaded.

    Args:
        session (Session): The SQLAlchemy session object for database operations.
        model (SQLModel): The SQLModel class representing the database table.
        file (str): The name of the JSON file containing the data to be loaded.

    Returns:
        None

    Raises:
        Exception: If there's an error during the data loading process, it's caught and logged.
    """
    try:
        statement = select(model)
        result = session.exec(statement).all()
        if not result:
            file_path = os.path.join(os.path.dirname(__file__), file)
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    data = json.load(file)
                    if data is None:
                        logger.warning("No data found in JSON file.")
                        return
                    for result in data:
                        result_obj = model(**result)
                        session.add(result_obj)
                        session.commit()
                        logger.info("Data loaded from JSON file successfully.")
            else:
                logger.warning("No data found in JSON file.")
        else:
            logger.info("Data already loaded in the database.")
    except Exception as e:
        logger.error(f"Error loading data from JSON file: {str(e)}")
