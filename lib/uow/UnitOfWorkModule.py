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
        Session = sessionmaker(bind=factory.getEngine())
        # pass the session object to the repositories
        self.roles_repo = RoleRepository(Session())
        self.semesters_repo = SemesterRepository(Session())
        self.students_repo = StudentRepository(Session())
        self.student_results_repo = StudentResultRepository(Session())
        self.student_semesters_repo = StudentSemesterRepository(Session())
        self.universities_repo = UniversityRepository(Session())
        self.users_repo = UserRepository(Session())
        self.user_roles_repo = UserRoleRepository(Session())

    def seed_default_entites(self):
        # seed default roles
        if len(self.roles_repo.get_all()) < 1:
            self.roles_repo.create(Role(name='admin'))
            self.roles_repo.create(Role(name='student'))
            self.roles_repo.create(Role(name='developer'))
        # seed default users
        if len(self.users_repo.get_all()) < 1:
            pass
