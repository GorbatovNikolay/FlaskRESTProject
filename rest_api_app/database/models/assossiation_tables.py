from sqlalchemy import Table, Column, ForeignKey

from .base_model import Base

students_and_courses = Table('students_and_courses', Base.metadata,
                             Column('student_id', ForeignKey('students.id'), primary_key=True),
                             Column('course_id', ForeignKey('courses.id'), primary_key=True)
                             )
