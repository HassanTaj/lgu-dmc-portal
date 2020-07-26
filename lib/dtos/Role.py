from lib.dtos.DeclarativeBaseContainer import *


class Role(Base):
    def __int__(self, id=None, name=None):
        self.id = id
        self.name = name

    __tablename__ = 'roles'
    id = Column(String, primary_key=True)
    name = Column(String(256))
