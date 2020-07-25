from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Semester(Base):
    def __int__(self, id=None, name=None):
        self.id = id
        self.name = name

    __tablename__ = 'semesters'
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
