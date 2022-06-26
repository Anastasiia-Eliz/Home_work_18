from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """Получить все жанры"""
        return self.session.query(Genre).all()

    def get_one(self, gid):
        """Получить по id"""
        return self.session.query(Genre).get(gid)