from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from flask_marshmallow import Marshmallow
# from lib.loaders import load_models
from flask import Flask

__all__ = ('db', 'init_db')

# app = Flask(__name__)

# database_host = "127.0.0.1:5432"
# database_name = "book_info"
# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{database_host}/{database_name}'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
# ma = Marshmallow(app)

# support importing a functioning session query
query = db.session.query

def init_db(app=None, db=None):
   """Initializes the global database object used by the app."""
   if isinstance(app, Flask) and isinstance(db, SQLAlchemy):
    #   load_models()
      db.init_app(app)
   else:
      raise ValueError('Cannot init DB without db and app objects.')