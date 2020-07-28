from lib.repositories.AppRepositories import *
from lib.helpers.ConnectionFactoryModule import *
from lib.helpers.ConnectionStringAdapterModule import *
from sqlalchemy.orm import sessionmaker


class UnitOfWork(object):
    def __init__(self, adapter: ConnectionStringAdapter = None):
        # get adapter
        self.connectionAdapter: ConnectionStringAdapter = adapter
        # get connection
        factory = ConnectionFactory(connection_adapter=self.connectionAdapter)
        # bind the engine with session
        Session = sessionmaker(bind=factory.get_engine())
        # pass the session object to the repositories
        self.roles_repo = RoleRepository(Session())
        self.semesters_repo = SemesterRepository(Session())
        self.students_repo = StudentRepository(Session())
        self.student_results_repo = StudentResultRepository(Session())
        self.universities_repo = UniversityRepository(Session())
        self.account_repo = AccountRepository(Session())

    def seed(self, doseed=False):
        if doseed:
            # Roles
            if len(self.roles_repo.get_all()) < 1:
                self.roles_repo.create(Role(name='admin'))
                self.roles_repo.create(Role(name='student'))
                self.roles_repo.create(Role(name='developer'))

            # Institutes
            if len(self.universities_repo.get_all()) < 1:
                self.universities_repo.create(University(name="LGU"))
                self.universities_repo.create(University(name="UCP"))
                self.universities_repo.create(University(name="UCF"))
                self.universities_repo.create(University(name="UOG"))
                self.universities_repo.create(University(name="MCU"))

            # seed default users
            if len(self.account_repo.get_all()) < 1:
                self.account_repo.create(Account(
                    user_name="leehaisen",
                    email='leehaisen01@gmail.com',
                    email_confirmed=True,
                    password='Abc123#',
                ))
                self.account_repo.create(Account(
                    user_name="developer",
                    email='developer@gmail.com',
                    email_confirmed=True,
                    password='Abc123#',
                ))

            # semesters
            if len(self.semesters_repo.get_all()) < 1:
                for i in range(1, 9, 1):
                    self.semesters_repo.create(Semester(number=f"""Semester {i}"""))
            # students
            if len(self.students_repo.get_all()) < 1:
                for i in range(1, 10):
                    self.students_repo.create(Student(
                        first_name=f'FN-{i}',
                        last_name=f'LN-{i}',
                        address=f'somewhere int the world {i}',
                        major=f'Computer Science',
                        gender='male'
                    ))
