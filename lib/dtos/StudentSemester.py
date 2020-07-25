from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class StudentSemester(Base):
    def __int__(self, id=None, name=None):
        pass

    __tablename__ = 'student_semesters'
    id = Column(String, primary_key=True)
    student_id = Column(String, ForeignKey('students.id'))
    student = relationship('Student')

    semester_id = Column(String, ForeignKey('semester.id'))
    semester = relationship('Semester')
