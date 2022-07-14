from flask import request, Flask, jsonify
from db import db

from models.publishers import Publishers


def publisher_delete(publisher_id):
    publisher_record = db.session.query(Publishers).filter(Publishers.publisher_id == publisher_id).first()

    if publisher_record:
        db.session.delete(publisher_record)
        db.session.commit()
        return jsonify('Publisher Deleted'), 200

    return jsonify('Publisher ID not found'), 404