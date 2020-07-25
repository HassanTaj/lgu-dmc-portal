from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    def __int__(self, id=None, name=None):
        self.id = id

    __tablename__ = 'students'
    id = Column(String, primary_key=True)
    first_name = Column(String(256), nullable=False)
    last_name = Column(String(256), nullable=False)
    address = Column(String(256), nullable=False)
    gender = Column(String(10), nullable=False)
    major = Column(String(100), nullable=False)
    # I have a question at this point will ask you when we are discussing this
    dob = Column(DateTime("%(day)02d-%(month)02d-%(year)04d"))
    email = Column(String(100), nullable=True)
