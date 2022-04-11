from sqlalchemy import select, func
from sqlalchemy.orm import Session

from database.models import Course, Group, Student


class MyQueries:
    """Class containing query functions."""

    @classmethod
    def get_groups_by_amount_of_students(cls, session: Session, amount_of_students: int) -> list:
        """Returns all groups with number of students less or equal than a given number."""
        stmt = select(Group, func.count(Student.id)).join(Group.students) \
            .group_by(Group.id).having(func.count(Student.id) <= amount_of_students)
        with session:
            return session.execute(stmt).all()

    @classmethod
    def get_students_by_course_name(cls, session: Session, course_name: str) -> list:
        """Returns all students connected with a given course."""
        stmt = select(Student).join(Student.courses.and_(Course.name == course_name))
        with session:
            return session.execute(stmt).scalars().all()

    @classmethod
    def add_new_student(cls, session: Session, first_name: str, last_name: str) -> None:
        """Adds a new student with a given name and last name to the database."""
        with session:
            session.add(Student(first_name=first_name, last_name=last_name))
            session.commit()

    @classmethod
    def delete_student_by_id(cls, session: Session, student_id: int) -> None:
        """Deletes a student with a given id from the database."""
        with session:
            student = session.get(Student, student_id)
            session.delete(student)
            session.commit()

    @classmethod
    def add_student_to_course(cls, session: Session, student_id: int, course_ids: list) -> None:
        """Adds a student to the courses with ids given in a list."""
        with session:
            student = session.get(Student, student_id)
            courses = [session.get(Course, course_id) for course_id in course_ids]
            student.courses.extend(courses)
            session.commit()

    @classmethod
    def remove_student_from_course(cls, session: Session, student_id: int, course_id: int) -> None:
        """Removes a student from the course."""
        with session:
            student = session.get(Student, student_id)
            course = session.get(Course, course_id)
            student.courses.remove(course)
            session.commit()
