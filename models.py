from sqlalchemy import (
    Table,
    Column,
    ForeignKey,
    Integer,
    String
)
from sqlalchemy.orm import (
    declarative_base,
    relationship
)

Base = declarative_base()
association_table = Table('association', Base.metadata,
                          Column('student_id', ForeignKey('student.id'), primary_key=True),
                          Column('course_id', ForeignKey('course.id'), primary_key=True)
                          )


class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    name = Column(String(5))

    students = relationship('Student', back_populates='group')

    def __repr__(self):
        return f'Address(id={self.id!r}, name={self.name!r})'


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    group_id = Column(Integer, ForeignKey('group.id'))

    group = relationship('Group', back_populates='students')
    courses = relationship('Course', secondary=association_table, back_populates='students')

    def __repr__(self):
        return f'User(id={self.id!r}, first name={self.first_name!r}, last name={self.last_name!r})'


class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    description = Column(String)

    students = relationship('Student', secondary=association_table, back_populates='courses')

    def __repr__(self):
        return f'''course id = {self.id!r}, name = {self.name!r} 
        description: {self.description!r}'''
