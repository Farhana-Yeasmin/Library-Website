





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