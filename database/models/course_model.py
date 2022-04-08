from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship

from .assossiation_tables import students_and_courses
from .base_model import Base


class Course(Base):
    name = Column(String(30))
    description = Column(Text)

    students = relationship('Student', secondary=students_and_courses, back_populates='courses')

    def __repr__(self):
        return f'Course(course id = {self.id!r}, name = {self.name!r}, description: {self.description!r})'
