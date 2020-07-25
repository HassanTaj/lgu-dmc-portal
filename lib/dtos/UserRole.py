from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class UserRole(Base):
    def __int__(self, id=None, user_id=None, role_id=None):
        self.id = id
        self.userId = user_id
        self.roleId = role_id

    __tablename__ = 'user_roles'
    id = Column(String, primary_key=True)

    user_id = Column(String, ForeignKey('users.id'))
    user = relationship('User')  # Table Class name

    role_id = Column(String, ForeignKey('roles.id'))
    role = relationship('Role')
