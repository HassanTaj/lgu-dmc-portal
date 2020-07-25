from sqlalchemy import Column, Integer, String , Boolean
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class University(Base):
    def __int__(self, id=None, name=None):
        self.id = id
        self.name = name

    __tablename__ = 'universities'
    id = Column(String, primary_key=True)
    name = Column(String(256))
