from flask import request, Flask, jsonify
from db import db

from models.books import Books


def book_update(book_id, author_id = None, publisher_id = None, title = None, languages = None, movie = None, genre = None):
    book_record = db.session.query(Books).filter(Books.book_id == book_id).first()

    if not book_record:
        return('Book not found'), 404
    if request:
        form = request.form
        author_id = form.get(author_id)
        publisher_id = form.get(publisher_id)
        title = form.get(title)
        languages = form.get(languages)
        movie = form.get(movie)
        genre = form.get(genre)

    if author_id:
        book_record.author_id = author_id
    if publisher_id:
        book_record.publisher_id = publisher_id
    if title:
        book_record.title = title
    if languages:
        book_record.languages = languages
    if movie:
        book_record.movie = movie
    if genre:
        book_record.genre = genre
 
    db.session.commit()

    return jsonify('Book Updated'), 201