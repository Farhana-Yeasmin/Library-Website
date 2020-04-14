from flask import Flask, request
from flask_restful import Api, Resource
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# api = Api(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
#
# db = SQLAlchemy(app)
# ma = Marshmallow(app)
#
#
# class Book(db.Model):
#     isbn = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     author = db.Column(db.String(100))
#     publisher = db.Column(db.String(100))
#
#
# class BookSchema(ma.Schema):
#     class Meta:
#         fields = ('isbn', 'name', 'author', 'publisher')
#
#
# db.create_all()
# db.session.commit()
#
# book_schema = BookSchema()
# books_schema = BookSchema(many=True)

# class BookResource(Resource):
#     def get(self):
#         # return {'data': 'get resource'}
#         return posts_schema.dumps(Book.query.all())
#
#     def post(self):
#         # return {'data': 'post resource'}
#         data = request.json
#         post = Book(isbn=data['isbn'], name=data['name'], author=data['author'], publisher=data['publisher'])
#         db.session.add(post)
#         db.session.commit()
#         return post_schema.dumps(post)
#
#
# api.add_resource(BookResource, '/books')
