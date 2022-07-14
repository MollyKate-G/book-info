from flask import request, Flask, jsonify
from db import db

from models.authors import Authors, author_schema


def author_get_one(author_id):
    author_record = db.session.query(Authors).filter(Authors.author_id == author_id).first()

    return jsonify(author_schema.dump(author_record)), 200
