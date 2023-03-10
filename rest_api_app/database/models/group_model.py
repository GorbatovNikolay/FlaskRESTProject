from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base_model import Base


class Group(Base):
    name = Column(String(5))

    students = relationship('Student', back_populates='group')

    def __repr__(self):
        return f'Group(id={self.id!r}, name={self.name!r})'
