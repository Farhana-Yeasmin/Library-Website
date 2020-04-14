from flask import Flask
from flask import Flask, request
from flask_restful import Api, Resource
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Book(db.Model):
    isbn = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    author = db.Column(db.String(100))
    publisher = db.Column(db.String(100))


class BookSchema(ma.Schema):
    class Meta:
        fields = ('isbn', 'name', 'author', 'publisher')


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))


class RoleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password')


role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)

book_schema = BookSchema()
books_schema = BookSchema(many=True)

db.create_all()
db.session.commit()


class RoleResource(Resource):

    def post(self):
        # return {'data': 'post resource'}
        data = request.json
        role = Role(id=data['id'], username=data['username'], password=data['password'])
        db.session.add(role)
        db.session.commit()
        return role_schema.dumps(role)

    def put(self):
        # return {'data': 'post resource'}
        data = request.json
        role = Role(id=data['id'], username=data['username'], password=data['password'])
        db.session.add(role)
        db.session.commit()
        return role_schema.dumps(role)

    def get(self, username):
        # user = Role.find_user_by_name(username)
        # if user:
        #     return user.json()
        return roles_schema.dumps(Role.query.all())


class BookResource(Resource):
    def get(self):
        # return {'data': 'get resource'}
        return books_schema.dumps(Book.query.all())

    def post(self):
        # return {'data': 'post resource'}
        data = request.json
        book = Book(isbn=data['isbn'], name=data['name'], author=data['author'], publisher=data['publisher'])
        db.session.add(book)
        db.session.commit()
        return book_schema.dumps(book)

    def put(self):
        data1 = request.json
        book = Book(isbn=data1['isbn'], name=data1['name'], author=data1['author'], publisher=data1['publisher'])
        db.session.add(book)
        db.session.commit()
        return book_schema.dumps(book)


api.add_resource(BookResource, '/books')
# api.add_resource(RoleResource, '/role/<string:username>')
api.add_resource(RoleResource, '/role')

if __name__ == '__main__':
    app.run(debug=True)
