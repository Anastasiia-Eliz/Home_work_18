from dao.genre_dao import GenreDAO


class GenreService:
	def __init__(self, dao: GenreDAO):
		self.dao = dao

	def get_all(self):
		"""Получить все жанры"""
		return self.dao.get_all()

	def get_one(self, gid):
		"""Получить по id"""
		return self.dao.get_one(gid)

