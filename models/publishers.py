from flask import request, Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import or_
import uuid
import marshmallow as ma
from db import db

app = Flask(__name__)

class Publishers(db.Model):
    __tablename__ = "publishers"
    publisher_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    publishing_company = db.Column(db.String(), nullable=False)
    first_publication = db.Column(db.String())
    active = db.Column(db.Boolean(), nullable=False, default = False)

    def __init__(self, publishing_company, first_publication, active = False):
        self.publishing_company = publishing_company
        self.first_publication = first_publication
        self.active = active


class PublisherSchema(ma.Schema):
    class Meta:
        fields = ['publisher_id', 'publishing_company','first_publication', 'active']
    

publisher_schema = PublisherSchema()
publishers_schema = PublisherSchema(many=True)