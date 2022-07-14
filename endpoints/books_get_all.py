from flask import request, Flask, jsonify
from db import db

from models.books import Books, books_schema


def books_get_all():
   book_records = db.session.query(Books).all()

   return jsonify(books_schema.dump(book_records)), 200
