from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from .ConnectionStringAdapterModule import ConnectionStringAdapter
from .ConnectionTypeModule import ConnectionType
from ..dtos.DeclarativeBaseContainer import Base


class ConnectionFactory(object):
    # initialize connection helper with connection string
    def __init__(self, connection_adapter: ConnectionStringAdapter = None):
        self.adapter: ConnectionStringAdapter = connection_adapter
        self.engine = create_engine(self.adapter.get_connection_string(), echo=False, check_same_thread=False if (
                    self.adapter.get_connection_type() == ConnectionType.sql_lite) else True)
        # Base.metadata.drop_all(bind=self.engine)
        print('should create database here')
        if not database_exists(self.engine.url):
            if self.adapter.get_connection_type() == ConnectionType.sql_lite:
                Base.metadata.create_all(bind=self.engine)
            elif self.adapter.get_connection_type() == ConnectionType.postgres_sql:
                create_database(self.engine.url)  # For postgres

    # get SqlAchemy Database Engine using this function
    def get_engine(self):
        try:
            # self.engine = create_engine(self.adapter.getConnectionString())
            return self.engine
        except Exception as engex:
            print(engex)

    # get connection object after connecting with database through engine
    def get_connection(self):
        try:
            return self.engine.connect()
        except Exception as ex:
            print(ex)
