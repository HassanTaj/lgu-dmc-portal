from lib.dtos.University import University
from lib.repositories.BaseRepository import BaseRepository


class UniversityRepository(BaseRepository):
    def __init__(self, session):
        self.session = session
        # initialize base repository
        super().__init__(self.session, University, True)