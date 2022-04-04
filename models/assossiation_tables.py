from sqlalchemy import Table, Column, ForeignKey

from models.base_model import Base

students_and_courses = Table('students_and_courses', Base.metadata,
                             Column('student_id', ForeignKey('student.id'), primary_key=True),
                             Column('course_id', ForeignKey('course.id'), primary_key=True)
                             )
