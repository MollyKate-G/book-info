from flask import request, Flask, jsonify
from db import db

from models.publishers import Publishers


def publisher_update(publisher_id, publishing_company = None, first_publication = None, active = None):
    publisher_record = db.session.query(Publishers).filter(Publishers.publisher_id == publisher_id).first()

    if not publisher_record:
        return('publisher not found'), 404
    if request:
        form = request.form
        publishing_company = form.get(publishing_company)
        first_publication = form.get(first_publication)
        active = form.get(active)

    if publishing_company:
        publisher_record.publishing_company = publishing_company
    if first_publication:
        publisher_record.first_publication = first_publication
    if active:
        publisher_record.active = active
 
    db.session.commit()

    return jsonify('Publisher Updated'), 201