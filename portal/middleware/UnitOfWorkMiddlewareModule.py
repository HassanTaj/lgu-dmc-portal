from django.utils.deprecation import MiddlewareMixin

from lib.uow.UnitOfWorkModule import UnitOfWork, ConnectionStringModel, ConnectionType, ConnectionStringAdapter

from portal.config import settings


class UnitOfWorkMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        # intialize unit of work
        self.uow: UnitOfWork = UnitOfWork(
            adapter=ConnectionStringAdapter(
                ConnectionStringModel(
                username=settings.DATABASE['user'],
                password=settings.DATABASE['password'],
                host=settings.DATABASE['host'],
                database=settings.DATABASE['database'],
                db_url=settings.SQLITE_DATABASE["url"]),
                ConnectionType.sql_lite)
        )
        # call the seed db method to seed default stuff in the db
        self.uow.seed_default_entites()
        # One-time configuration and initialization.

    def process_request(self, request):
        request.uow = self.uow
        return None

    # def process_response(self, request, response):
    #     try:
    #         session = request.db_session
    #     except AttributeError:
    #         return response
    #     try:
    #         session.commit()
    #         return response
    #     except:
    #         # session.rollback()
    #         raise

# def process_exception(self, request, exception):
#     try:
#         session = request.db_session
#     except AttributeError:
#         return
# # session.rollback()
