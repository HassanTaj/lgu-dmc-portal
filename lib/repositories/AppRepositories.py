from lib.dtos.Role import Role
from lib.dtos.Semester import Semester
from lib.dtos.Student import Student
from lib.dtos.StudentResult import StudentResult
from lib.dtos.University import University
from lib.dtos.Account import Account
from lib.repositories.BaseRepository import *


class SemesterRepository(BaseRepository):
    def __init__(self, session):
        self.session = session
        super().__init__(self.session, Semester, True)


class StudentRepository(BaseRepository):
    def __init__(self, session):
        self.session = session
        super().__init__(self.session, Student, True)


class StudentResultRepository(BaseRepository):
    def __init__(self, session):
        self.session = session
        super().__init__(self.session, StudentResult, True)


class UniversityRepository(BaseRepository):
    def __init__(self, session):
        self.session = session
        super().__init__(self.session, University, True)


class AccountRepository(BaseRepository):
    def __init__(self, session):
        self.session = session
        super().__init__(self.session, Account, True)

    def get_by_username_or_password(self, uname, pswd):
        try:
            res = self._session.query(self.query_type).filter(
                self.query_type.user_name == uname and self.query_type.password == pswd)
            return res[0]
        except Exception as ex:
            print(ex)


class RoleRepository(BaseRepository):
    def __init__(self, session):
        self.session = session
        super().__init__(self.session, Role, True)