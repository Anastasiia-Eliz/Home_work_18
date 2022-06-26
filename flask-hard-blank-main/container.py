from dao.movie_dao import MovieDAO
from service.movies import MovieService
from setup_db import db
from dao.genre_dao import GenreDAO
from service.genres import GenreService
from dao.director_dao import DirectorDAO
from service.directors import DirectorService

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)