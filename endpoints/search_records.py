from flask import request, Flask, jsonify
from db import db

from models.books import Books, books_schema
from models.authors import Authors
from models.publishers import Publishers


def search_records(search_term):
   results = []
   if search_term:
      search_term = search_term.lower()

      results = db.session.query(Books) or db.session.query(Authors) or db.session.query(Publishers)\
         .filter(db.or_( \
            db.func.lower(Books.title).contains(search_term), \
            db.func.lower(Books.languages).contains(search_term), \
            db.func.lower(Books.movie).contains(search_term), \
            db.func.lower(Books.genre).contains(search_term), \
            db.func.lower(Authors.name).contains(search_term), \
            db.func.lower(Authors.birth_location).contains(search_term), \
            db.func.lower(Authors.quote).contains(search_term),
            db.func.lower(Publishers.publishing_company).contains(search_term),
            db.func.lower(Publishers.active).contains(search_term))) \
         .all()
   else:
      return jsonify('No search term sent'), 400
   return jsonify(books_schema.dump(results)), 200