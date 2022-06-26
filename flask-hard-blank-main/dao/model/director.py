from setup_db import db
from marshmallow import Schema, fields


class Director(db.Model):
	__tablename__ = 'director'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)

class DirectorSchema(Schema):
	__tablename__ = 'director'
	id = fields.Int()
	name = fields.String()