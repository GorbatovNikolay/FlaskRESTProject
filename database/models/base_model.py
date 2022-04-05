from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.orm import declarative_base, declared_attr
from sqlalchemy.schema import Sequence


class Base(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, Sequence(__name__.lower() + '_id_seq'), primary_key=True)


Base = declarative_base(cls=Base)
