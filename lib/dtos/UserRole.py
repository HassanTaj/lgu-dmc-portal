from sqlalchemy import Column, Integer, String , Boolean, DateTime,ForeignKey
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class UserRole(Base):
    def __int__(self, id=None, name=None):
        pass

    __tablename__ = 'user_role'
    rol_id=Column(String,primary_key=True)
    roles=Column(String)


