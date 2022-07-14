from flask import request, Flask, jsonify
from db import db

from models.publishers import Publishers, publishers_schema


def publishers_get_all():
   publisher_records = db.session.query(Publishers).all()

   return jsonify(publishers_schema.dump(publisher_records)), 200