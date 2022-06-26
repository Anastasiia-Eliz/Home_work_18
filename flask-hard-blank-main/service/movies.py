# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

from dao.movie_dao import MovieDAO
from dao.model.movie import Movie


class MovieService:
	def __init__(self, dao: MovieDAO):
		self.dao = dao

	def get_all(self, director_id, genre_id, year):
		"""Получить все фильмы,все фильмы режиссера, все фильмы жанра, все фильмы за год"""
		if director_id:
			all_movies = self.dao.get_by_director(director_id)
			return all_movies
		if genre_id:
			all_movies = self.dao.get_by_genre(genre_id)
			return all_movies
		if year:
			all_movies = self.dao.get_by_year(year)
			return all_movies
		all_movies = self.dao.get_all()
		return all_movies

	def get_one(self, mid):
		"""Получить фильм по id"""
		return self.dao.get_one(mid)


	def create(self, data):
		"""Создать фильм"""
		return self.dao.create(data)


	def update(self, data):
		"""Обновить фильм"""
		mid = data.get("id")
		movie = self.session.query(Movie).get(mid)
		movie.title = data.get("title")
		movie.description = data.get("description")
		movie.trailer = data.get("trailer")
		movie.year = data.get("year")
		movie.rating = data.get("rating")
		movie.genre_id = data.get("genre_id")
		movie.director_id = data.get("director_id")
		self.dao.update(movie)


	def delete(self, mid):
		"""Удалить фильм"""
		movie = self.get_one(mid)
		self.dao.delete(movie)
