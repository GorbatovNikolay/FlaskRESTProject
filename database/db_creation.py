from sqlalchemy import create_engine

from .models import Base


def create_tables():
    """Creates tables from models."""
    engine = create_engine(
        'postgresql+psycopg2://my_user:resuetaerc@localhost:5432/task_10',
        echo=True, future=True
    )
    Base.metadata.create_all(engine)


def populate_db():
    pass


def create_db():
    create_tables()


if __name__ == '__main__':
    create_db()
