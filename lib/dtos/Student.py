from lib.dtos.DeclarativeBaseContainer import *


class Student(Base):
    def __int__(self, id=None, first_name=None, last_name=None, roll_number=None,
                address=None, gender=None, major=None, university_id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.gender = gender
        self.major = major

    __tablename__ = 'students'
    id = Column(String, primary_key=True)
    first_name = Column(String(256), nullable=False)
    last_name = Column(String(256), nullable=False)
    roll_number = Column(String(256), nullable=False)
    address = Column(String(256), nullable=False)
    gender = Column(String(10), nullable=False)
    major = Column(String(100), nullable=False)

    university_id = Column(String, ForeignKey('universities.id'))
    results = relationship('lib.dtos.StudentResult.StudentResult', backref="students")

# class Parent(Base):
#     __tablename__ = 'parent'
#     id = Column(Integer, primary_key=True)
#     child_id = Column(Integer, ForeignKey('child.id'))
#     child = relationship("Child", back_populates="parent")
# 
# class Child(Base):
#     __tablename__ = 'child'
#     id = Column(Integer, primary_key=True)
#     parent = relationship("Parent", back_populates="child", uselist=False)
