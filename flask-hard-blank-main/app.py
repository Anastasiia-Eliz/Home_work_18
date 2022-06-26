from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.director import director_ns
from views.genre import genres_ns
from views.movie import movies_ns
from create_data import create_db_in_memory

def create_app(config: Config) -> Flask:
	application = Flask(__name__)
	application.config.from_object(config)
	application.app_context().push()
	configure_app(application)
	return application


def configure_app(application: Flask):
	db.init_app(application)
	api = Api(application)
	api.add_namespace(director_ns)
	api.add_namespace(genres_ns)
	api.add_namespace(movies_ns)
	create_data(application)

def create_data(app):
	with app.app_context():
		create_db_in_memory()

app = create_app(Config())
app.debug = True




if __name__ == '__main__':
	app = create_app(Config())
	app.run()
