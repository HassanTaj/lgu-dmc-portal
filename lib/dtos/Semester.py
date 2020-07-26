from lib.dtos.DeclarativeBaseContainer import *


class Semester(Base):
    def __int__(self, id=None, name=None):
        self.id = id
        self.name = name

    __tablename__ = 'semesters'
    id = Column(String, primary_key=True)
    number = Column(String, nullable=False)
