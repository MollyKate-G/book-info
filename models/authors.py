from flask import request, Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import or_
import uuid
import marshmallow as ma
from db import db

app = Flask(__name__)


class Authors(db.Model):
    __tablename__ = "authors"
    author_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = db.Column(db.String(), nullable=False)
    birthdate = db.Column(db.String(), nullable = False)
    death_date = db.Column(db.String())
    birth_location = db.Column(db.String())
    quote = db.Column(db.String())
    active = db.Column(db.Boolean(), default = False)
    books = db.relationship('Books', cascade="all,delete", backref = 'author', lazy = True)

    def __init__(self, name, birthdate, death_date, birth_location, quote, active):
        self.name = name
        self.birthdate = birthdate
        self.death_date = death_date
        self.birth_location = birth_location
        self.quote = quote
        self.active = active


class AuthorSchema(ma.Schema):
    class Meta:
        fields = ['author_id', 'name', 'birthdate', 'death_date', 'birth_location', 'quote', 'active']

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)