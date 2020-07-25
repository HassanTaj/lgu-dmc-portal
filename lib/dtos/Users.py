from sqlalchemy import Column, Integer, String , Boolean, DateTime,ForeignKey
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Users(Base):
    def __int__(self, id=None, name=None):
        pass

    __tablename__ = 'users'
    rol_id=Column(String,ForeignKey='user_role.rol_id')
    # STILL CONFUSED ON THIS PART


