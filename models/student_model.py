from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.assossiation_tables import students_and_courses
from models.base_model import Base


class Student(Base):
    first_name = Column(String(30))
    last_name = Column(String(30))
    group_id = Column(Integer, ForeignKey('group.id'))

    group = relationship('Group', back_populates='students')
    courses = relationship('Course', secondary=students_and_courses, back_populates='students')

    def __repr__(self):
        return f'User(id={self.id!r}, first name={self.first_name!r}, last name={self.last_name!r})'
