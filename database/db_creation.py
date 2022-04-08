from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base
from objects import db_objects

engine = create_engine(
    'postgresql+psycopg2://my_user:resuetaerc@localhost:5432/task_10',
    echo=True, future=True
)


def create_tables() -> None:
    """Creates tables from models."""
    Base.metadata.create_all(engine)


def populate_db() -> None:
    """Inserts instances of models to tables."""
    session = Session(bind=engine)
    for objects in db_objects:
        session.add_all(objects)
    session.commit()
    session.close()


def create_db() -> None:
    """Sets up the tables."""
    create_tables()
    populate_db()


def delete_tables() -> None:
    """Deletes all created tables."""
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    create_db()
