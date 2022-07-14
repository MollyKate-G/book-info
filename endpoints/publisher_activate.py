from flask import request, Flask, jsonify
from db import db

from models.publishers import Publishers


def publisher_activate(publisher_id):
    publisher_record = db.session.query(Publishers).filter(Publishers.publisher_id == publisher_id).first()
    if not publisher_record:
        return ('Publisher not found'), 404
        
    publisher_record.active = True
    db.session.commit()

    return jsonify("Publisher Activated"), 201