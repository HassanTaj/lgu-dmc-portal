from lib.dtos.DeclarativeBaseContainer import *


class Account(Base):
    def __int__(self, id=None, user_name=None, email=None,
                email_confirmed=None, password=None, password_hash=None,
                student_id=None, role_id=None, university_id=None):
        self.id = id
        self.user_name = user_name
        self.password = password
        self.password_hash = password_hash
        self.email = email
        self.email_confirmed = email_confirmed
        self.student_id = student_id
        self.role_id = role_id
        self.university_id = university_id

    __tablename__ = 'accounts'
    id = Column(String, primary_key=True)
    user_name = Column(String(50))
    password = Column(String)
    password_hash = Column(String)
    dob = Column(DateTime("%(day)02d-%(month)02d-%(year)04d"))
    email = Column(String(100), nullable=True)
    email_confirmed = Column(Boolean, nullable=True)

    student_id = Column(String, ForeignKey('students.id'), nullable=True)
    # student = relationship('lib.dtos.Student.Student')

    role_id = Column(String, ForeignKey('roles.id'), nullable=True)
    # user_role = relationship("lib.dtos.UserRole.UserRole",back_populates="users")

    university_id = Column(String, ForeignKey('universities.id'), nullable=True)
