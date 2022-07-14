from flask import request, Flask, jsonify
from db import db

from models.books import Books, book_schema


def book_get_one(book_id):
    book_record = db.session.query(Books).filter(Books.book_id == book_id).first()

    return jsonify(book_schema.dump(book_record)), 200