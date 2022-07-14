from flask import request, Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy import or_
# import uuid
# import marshmallow as ma
from db import db

from models.authors import Authors

app = Flask(__name__)


@app.route('/delete_author/<author_id>', methods=['DELETE'])
def author_delete(author_id):
    author_record = db.session.query(Authors).filter(Authors.author_id == author_id).first()

    if author_record:
        db.session.delete(author_record)
        db.session.commit()
        return jsonify('Author Deleted'), 200

    return jsonify('Author ID not found'), 404