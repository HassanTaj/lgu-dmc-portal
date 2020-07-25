from lib.dtos.Role import Role
from lib.dtos.Semester import Semester
from lib.dtos.Student import Student
from lib.dtos.StudentResult import StudentResult
from lib.dtos.StudentSemester import StudentSemester
from lib.dtos.University import University
from lib.dtos.User import User
from lib.dtos.UserRole import UserRole
from lib.repositories.BaseRepository import BaseRepository


class SemesterRepository(BaseRepository):
    def __init__(self, session):
        self.session = session
        super().__init__(self, Semester, True)


class StudentRepository(BaseRepository):
    def __init__(self, session):
        self.session = session
        super().__init__(self, Student, True)


class StudentResultRepository(BaseRepository):
    def __init__(self, session):
        self.session = session
        super().__init__(self, StudentResult, True)


class StudentSemesterRepository(BaseRepository):
    def __init__(self, session):
        self.session = session
        super().__init__(self, StudentSemester, True)


class StudentSemesterRepository(BaseRepository):
    def __init__(self, session):
        self.session = session
        super().__init__(self, StudentSemester, True)


class UniversityRepository(BaseRepository):
    def __init__(self, session):
        self.session = session
        super().__init__(self.session, University, True)


class UserRepository(BaseRepository):
    def __init__(self, session):
        self.session = session
        super().__init__(self.session, User, True)


class UserRoleRepository(BaseRepository):
    def __init__(self, session):
        self.session = session
        super().__init__(self.session, UserRole, True)


class RoleRepository(BaseRepository):
    def __init__(self, session):
        self.session = session
        super().__init__(self, Role, True)
