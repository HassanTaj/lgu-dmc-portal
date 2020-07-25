from sqlalchemy import Column, Integer, String , Boolean
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class University(Base):
    def __int__(self, id=None, name=None):
        pass

    __tablename__ = 'universities'
    uni_id = Column(String, primary_key=True)
    uni_name = Column(String)
