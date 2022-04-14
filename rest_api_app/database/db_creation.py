from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .models import Base, Course, Group, Student
from .processors import db_objects
from .processors.consts import CONNECTION_STR
from .processors.student_processor import FillStudentProcessor

engine = create_engine(
    CONNECTION_STR,
    echo=True, future=True
)
Base.metadata.bind = engine
session = Session(bind=engine)


def create_tables() -> None:
    """Creates tables from models."""
    Base.metadata.create_all(engine)


def populate_db() -> None:
    """Inserts instances of models to tables."""

    FillStudentProcessor.assign_courses_to_students(db_objects[1], db_objects[2])
    for objects, table in zip(db_objects, [Group, Student, Course]):
        if not session.query(table).first():
            session.add_all(objects)

    session.commit()
    session.close()


def create_db() -> None:
    """Sets up the tables."""
    create_tables()
    populate_db()
