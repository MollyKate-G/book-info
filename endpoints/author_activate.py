from flask import request, Flask, jsonify
from db import db

from models.authors import Authors


def author_activate(author_id):
    author_record = db.session.query(Authors).filter(Authors.author_id == author_id).first()
    if not author_record:
        return ('Author not found'), 404
        
    author_record.active = True
    db.session.commit()

    return jsonify("Author Activated"), 201