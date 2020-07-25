from sqlalchemy import Column, Integer, String , Boolean, DateTime,ForeignKey
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Student_semester(Base):
    def __int__(self, id=None, name=None):
        pass

    __tablename__ = 'std_semester'
    std_id = Column(String,ForeignKey='students.std_id')
    sem_id = Column(String,ForeignKey='semester.sem_id')



