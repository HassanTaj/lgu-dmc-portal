from sqlalchemy import Column, Integer, String , Boolean, DateTime,ForeignKey
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Student_Result(Base):
    def __int__(self, id=None, name=None):
        pass

    __tablename__ = 'student_results'
    std_res_id = Column(String,primary_key=True)
    std_id = Column(String,ForeignKey='students.std_id')
    res_path = Column(String)

