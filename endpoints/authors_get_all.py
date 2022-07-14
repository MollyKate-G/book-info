from flask import request, Flask, jsonify
from db import db

from models.authors import Authors, authors_schema


def authors_get_all():
   author_records = db.session.query(Authors).all()

   return jsonify(authors_schema.dump(author_records)), 200