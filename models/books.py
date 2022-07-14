from turtle import pu
from flask import request, Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import or_
import uuid
import marshmallow as ma
from db import db

from .authors import AuthorSchema, Authors
from .publishers import PublisherSchema, Publishers

app = Flask(__name__)

class Books(db.Model):
    __tablename__ = "books"
    book_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    author_id = db.Column(UUID(as_uuid=True), db.ForeignKey('authors.author_id'))
    publisher_id =  db.Column(UUID(as_uuid=True), db.ForeignKey('publishers.publisher_id'))
    title = db.Column(db.String(), nullable = False)
    languages = db.Column(db.String())
    movie = db.Column(db.Boolean())
    genre = db.Column(db.String())
    authors = db.relationship('Authors', cascade="all,delete", backref = 'authors')
    publishers = db.relationship('Publishers', cascade="all,delete", backref = 'publishers')

    def __init__(self, author_id, publisher_id, title, languages, movie, genre):
        self.author_id = author_id
        self.publisher_id = publisher_id
        self.title = title
        self.languages = languages
        self.movie = movie
        self.genre = genre

class BookSchema(ma.Schema):
    class Meta:
        fields = ['book_id', 'title', 'languages', 'movie', 'genre', 'publisher', 'author']

    publisher = ma.fields.Nested(PublisherSchema(only=('publishing_company','active')))
    author = ma.fields.Nested(AuthorSchema(only=('name','birth_location', 'quote')))

book_schema = BookSchema()
books_schema = BookSchema(many=True)