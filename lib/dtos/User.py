from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    def __int__(self, id=None, user_name=None, password=None, password_hash=None, student_id=None, user_role_id=None):
        self.id = id

    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    user_name = Column(String(50))
    password = Column(String)
    password_hash = Column(String)

    student_id = Column(String, ForeignKey('students.id'))
    student = relationship('Student')

    user_role_id = Column(String, ForeignKey('user_role.id'))
    user_role = relationship("UserRole")
