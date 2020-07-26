from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from .ConnectionStringAdapterModule import ConnectionStringAdapter
from ..dtos.DeclarativeBaseContainer import Base


class ConnectionFactory(object):
    # initialize connection helper with connection string
    def __init__(self, connection_adapter: ConnectionStringAdapter = None):
        self.adapter: ConnectionStringAdapter = connection_adapter
        self.engine = create_engine(self.adapter.getConnectionString(), echo=True)

        print('should create database here')
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
            Base.metadata.create_all(bind=self.engine)

        # Base.metadata.drop_all(bind=self.engine)
        # Base.metadata.create_all(bind=self.engine)

    # get SqlAchemy Database Engine using this function
    def getEngine(self):
        try:
            # self.engine = create_engine(self.adapter.getConnectionString())
            return self.engine
        except Exception as engex:
            print(engex)

    # get connection object after connecting with database through engine
    def getConnection(self):
        try:
            return self.engine.connect()
        except Exception as ex:
            print(ex)
