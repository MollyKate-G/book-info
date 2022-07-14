from flask import request, Flask, jsonify
from db import db

from models.authors import Authors


def author_update(author_id, name = None, birthdate = None, death_date = None, birth_location = None, quote = None, active = None):
    author_record = db.session.query(Authors).filter(Authors.author_id == author_id).first()

    if not author_record:
        return('author not found'), 404
    if request:
        form = request.form
        name = form.get(name)
        birthdate = form.get(birthdate)
        death_date = form.get(death_date)
        birth_location = form.get(birth_location)
        quote = form.get(quote)
        active = form.get(active)

    if name:
        author_record.name = name
    if birthdate:
        author_record.birthdate = birthdate
    if death_date:
        author_record.death_date = death_date
    if birth_location:
        author_record.birth_location = birth_location
    if quote:
        author_record.quote = quote
    if active:
        author_record.active = active
 
    db.session.commit()

    return jsonify('Author Updated'), 201