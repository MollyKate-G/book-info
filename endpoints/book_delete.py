from flask import request, Flask, jsonify
from db import db

from models.books import Books


def book_delete(book_id):
    book_record = db.session.query(Books).filter(Books.book_id == book_id).first()

    if book_record:
        db.session.delete(book_record)
        db.session.commit()
        return jsonify('Book Deleted'), 200

    return jsonify('Book ID not found'), 404