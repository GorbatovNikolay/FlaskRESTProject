from sqlalchemy import select, func
from sqlalchemy.orm import Session

from rest_api_app.database.models import Course, Group, Student


class MyQueries:
    """Class containing query functions."""

    @classmethod
    def get_groups_by_amount_of_students(cls, session: Session, amount_of_students: int) -> dict:
        """Returns all groups with number of students less or equal than a given number."""
        stmt = select(Group).join(Group.students) \
            .group_by(Group.id).having(func.count(Student.id) <= amount_of_students)
        with session:
            result = session.execute(stmt).scalars().all()
            if result:
                return {
                    'data': [{'group_id': group.id, 'group_name': group.name} for group in result]
                }
            return {'message': 'There are no matching groups.'}

    @classmethod
    def get_students_by_course_name(cls, session: Session, course_name: str) -> dict:
        """Returns all students connected with a given course."""
        stmt = select(Student).join(Student.courses.and_(Course.name == course_name))
        with session:
            result = session.execute(stmt).scalars().all()
            if result:
                return {
                    'data': [{
                        'student_id': student.id, 'first_name': student.first_name, 'last_name': student.last_name
                    } for student in result]
                }
            return {'message': f'There is no {course_name} course.'}

    @classmethod
    def add_new_student(cls, session: Session, first_name: str, last_name: str) -> dict:
        """Adds a new student with a given name and last name to the database."""
        with session:
            student = Student(first_name=first_name.title(), last_name=last_name.title())
            session.add(student)
            session.commit()
            return {
                'message':
                    f'Student first_name={student.first_name} last_name={student.last_name} '
                    f'id={student.id} has been added.'
            }

    @classmethod
    def delete_student_by_id(cls, session: Session, student_id: int) -> dict:
        """Deletes a student with a given id from the database."""
        with session:
            student = session.get(Student, student_id)
            if student:
                session.delete(student)
                session.commit()
                return {'message': f'Student id={student_id} has been deleted.'}
            return {'message': f'Student id={student_id} does not exist.'}

    @classmethod
    def add_student_to_course(cls, session: Session, student_id: int, course_ids: list) -> dict:
        """Adds a student to the courses with ids given in a list."""
        with session:
            student = session.get(Student, student_id)
            if not student:
                return {'message': f'Student id={student_id} does not exist.'}
            courses = [session.get(Course, course_id) for course_id in course_ids]
            student.courses.extend(courses)
            session.commit()
            return {'message': f'Student id={student.id} has been enrolled to chosen courses.'}

    @classmethod
    def generate_response(cls, session: Session, student: Student, course: Course) -> dict:
        if course not in student.courses:
            return {'message': f'Student id={student.id} does not attend course id={course.id}.'}

        student.courses.remove(course)
        session.commit()
        return {'message': f'Student id={student.id} was removed from the {course.name} course.'}

    @classmethod
    def remove_student_from_course(cls, session: Session, student_id: int, course_id: int) -> dict:
        """Removes a student from the course."""
        with session:
            student = session.get(Student, student_id)
            if not student:
                return {'message': f'There is no such student id={student_id}'}

            course = session.get(Course, course_id)
            if not course:
                return {'message': f'There is no such course id={course_id}'}

            return cls.generate_response(session, student, course)
