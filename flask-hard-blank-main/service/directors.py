from dao.director_dao import DirectorDAO


class DirectorService:
	def __init__(self, dao: DirectorDAO):
		self.dao = dao

	def get_all(self):
		"""Получить всех режиссеров"""
		return self.dao.get_all()

	def get_one(self, uid):
		"""Получить по id"""
		return self.dao.get_one(uid)