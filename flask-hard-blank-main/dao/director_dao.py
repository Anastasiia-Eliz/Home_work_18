from dao.model.director import Director


class DirectorDAO:
	def __init__(self, session):
		self.session = session

	def get_all(self):
		"""Получить всех режиссеров"""
		return self.session.query(Director).all()

	def get_one(self, uid):
		"""Получить по id """
		return self.session.query(Director).get(uid)
