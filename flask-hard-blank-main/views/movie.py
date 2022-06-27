from flask_restx import Resource, Namespace
from flask import request
from dao.model.movie import MovieSchema, Movie
from container import movie_service


movies_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route('/')
class MoviesView(Resource):
	def get(self):
		director_id = request.args.get('director_id')
		genre_id = request.args.get('genre_id')
		year = request.args.get('year')
		return movies_schema.dump(movie_service.get_all(director_id, genre_id, year)), 200

	def post(self):
		data = request.get_json()
		movie_service.create(data)

		return "", 201


@movies_ns.route('/<int:mid>')
class MovieView(Resource):
	def get(self, mid):
		movie = movie_service.get_one(mid)
		return movie_schema.dump(movie), 200

	def put(self, mid):
		req_json = request.json
		movie_service.update(req_json, mid)
		return "", 204

	def delete(self, mid):
		movie_service.delete(mid)
		return '', 204
