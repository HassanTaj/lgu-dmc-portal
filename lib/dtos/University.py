from lib.dtos.DeclarativeBaseContainer import *


class University(Base):
    def __int__(self, id=None, name=None):
        self.id = id
        self.name = name

    __tablename__ = 'universities'
    id = Column(String, primary_key=True)
    name = Column(String(256))
