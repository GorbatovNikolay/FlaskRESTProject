from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base, Course, Group, Student
from objects import db_objects
from objects.student_objects_creation import assign_courses_to_students

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

    assign_courses_to_students(db_objects[1], db_objects[2])
    for objects, table in zip(db_objects, [Group, Student, Course]):
        if not session.query(table).first():
            session.add_all(objects)

    session.commit()
    session.close()


def create_db() -> None:
    """Sets up the tables."""
    create_tables()
    populate_db()


if __name__ == '__main__':
    create_db()
