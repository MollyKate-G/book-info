from flask import request, Flask, jsonify
from db import db

from models.publishers import Publishers, publisher_schema


def publisher_get_one(publisher_id):
    publisher_record = db.session.query(Publishers).filter(Publishers.publisher_id == publisher_id).first()

    return jsonify(publisher_schema.dump(publisher_record)), 200
