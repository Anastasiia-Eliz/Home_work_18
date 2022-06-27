from dao.model.movie import Movie
from dao.model.director import Director
from dao.model.genre import Genre


class MovieDAO:
	def __init__(self, session):
		self.session = session

	def get_all(self):
		"""Получить все фильмы"""
		return self.session.query(Movie).all()

	def get_one(self, mid):
		"""Получить фильм по id """
		return self.session.query(Movie).get(mid)


	def get_by_year(self, year):
		"""Получить все фильмы за год"""
		return self.session.query(Movie).filter(Movie.year == year).all()

	def get_by_genre(self, genre_id):
		"""Получить все фильмы жанра"""
		return self.session.query(Movie).filter(Genre.id == genre_id).join(Genre).all()

	def get_by_director(self, director_id):
		"""Получить все фильмы режиссера"""
		return self.session.query(Movie).filter(Director.id == director_id).join(Director).all()

	def create(self, data):
		"""Создать фильм"""
		new_movie = Movie(**data)
		self.session.add(new_movie)
		self.session.commit()
		return new_movie


	def update(self, movie):
		"""Обновить фильм"""
		self.session.add(movie)
		self.session.commit()

		return movie


	def delete(self, mid):
		"""Удалить фильм"""
		movie = self.get_one(mid)

		self.session.delete(movie)
		self.session.commit()
