from sqlalchemy import Column, Integer, String , Boolean, DateTime
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Semester(Base):
    def __int__(self, id=None, name=None):
        pass

    __tablename__ = 'semester'
    sem_id = Column(String, primary_key=True)
    semesters = Column(String,nullable=False)

