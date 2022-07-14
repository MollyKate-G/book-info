from flask import request, Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import or_
import uuid
from datetime import datetime
import marshmallow as ma
from db import db, init_db

from models.authors import Authors, author_schema, authors_schema, AuthorSchema
from models.books import Books, books_schema, book_schema, BookSchema
from models.publishers import Publishers, publisher_schema, publishers_schema, PublisherSchema
import endpoints

app = Flask(__name__)

database_host = "127.0.0.1:5432"
database_name = "book_info"
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{database_host}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
init_db(app,db)

# db = SQLAlchemy(app)
ma = Marshmallow(app)



def create_all():
    with app.app_context():
        db.create_all()

        print("Querying for authors...")
        author_data = db.session.query(Authors).filter(Authors.name == "C.S. Lewis").first()
        if author_data == None:
            print("The author C.S. Lewis was not found. Creating C.S. Lewis's information in the database...")
            
            author_data = Authors('C.S. Lewis', '29 November 1898', '22 November 1963', 
                                    'Belfast, United Kingdom', 'The more often he feels without acting, the less he will be able ever to act, and, in the long run, the less he will be able to feel.', False)

            db.session.add(author_data)
            db.session.commit()
        else:
            print("C.S. Lewis found!")




        print("Querying for publishers...")
        publisher_data = db.session.query(Publishers).filter(Publishers.publishing_company == "Geoffrey Bles").first()
        if publisher_data == None:
        
            print("The publisher Geoffrey Bles was not found. Creating Geoffrey Bles's information in the database...")
            
            publisher_data = Publishers('Geoffrey Bles', '1942', False)

            db.session.add(publisher_data)
            db.session.commit()
        else:
            print("Geoffrey Bles has been found!")




        print("Querying for books...")
        book_data = db.session.query(Books).filter(Books.title == "The Screw Tape Letters").first()
        if book_data == None:
            author_id = author_data.author_id
            publisher_id = publisher_data.publisher_id
        
            print("The book The Screw Tape Letters was not found. Creating The Screw Tape Letters information in the database...")
            
            book_data = Books(author_id, publisher_id, 'The Screw Tape Letters', '1', False, 'Epistolary novel')

            db.session.add(book_data)
            db.session.commit()
        else:
            print("The Screw Tape Letters have been found!")



@app.route('/author/activate/<author_id>', methods=['PUT'])
def author_activate(author_id):
    return endpoints.author_activate(author_id)


@app.route('/author/deactivate/<author_id>', methods=['PUT'])
def author_deactivate(author_id):
     return endpoints.author_deactivate(author_id)


@app.route('/delete_author/<author_id>', methods=['DELETE'])
def author_delete(author_id):
    return endpoints.author_delete(author_id)
    

@app.route('/authors/<author_id>', methods=['GET'])
def author_get_one(author_id):
    return endpoints.author_get_one(author_id)


# Doesn't update author but gives 201 status
@app.route('/author/update/<author_id>', methods=['PUT'])
def author_update(author_id, name = None, birthdate = None, death_date = None, birth_location = None, quote = None, active = None):    
    return endpoints.author_update(author_id)


@app.route('/authors/list', methods=['GET'])
def authors_get_all():
    return endpoints.authors_get_all()


@app.route('/delete_book/<book_id>', methods=['DELETE'])
def book_delete(book_id):
    return endpoints.book_delete(book_id)

@app.route('/book/<book_id>', methods=['GET'])
def book_get_one(book_id):
    return endpoints.book_get_one(book_id)


# Doesn't update a book but gives 201 status
@app.route('/book/update/<book_id>', methods=['PUT'])
def book_update(book_id, author_id = None, publisher_id = None, title = None, languages = None, movie = None, genre = None):
     return endpoints.book_update(book_id)


@app.route('/book/list', methods=['GET'])
def books_get_all():
    return endpoints.books_get_all()


@app.route('/publisher/activate/<publisher_id>', methods=['PUT'])
def publisher_activate(publisher_id):
    return endpoints.publisher_activate(publisher_id)

# ********
@app.route('/publisher/deactivate/<publisher_id>', methods=['PUT'])
def publisher_deactivate(publisher_id):
    return endpoints.publisher_deactivate(publisher_id)


@app.route('/delete_publisher/<publisher_id>', methods=['DELETE'])
def publisher_delete(publisher_id):
    return endpoints.publisher_delete(publisher_id)


@app.route('/publisher/<publisher_id>', methods=['GET'])
def publisher_get_one(publisher_id):
    return endpoints.publisher_get_one(publisher_id)


@app.route('/publisher/update/<publisher_id>', methods=['PUT'])
def publisher_update(publisher_id, publishing_company = None, first_publication = None, active = None):
    return endpoints.publisher_update(publisher_id)

@app.route('/publisher/list', methods=['GET'])
def publishers_get_all():
    return endpoints.publishers_get_all()

# Nested fields aren't showing up
@app.route('/search/<search_term>', methods=['GET'])
def search_records(search_term):
    return endpoints.search_records(search_term)



if __name__ == '__main__':
  create_all()
  app.run()