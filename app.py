from flask import Flask
from flask_restful import Api

from resources.article_resource import ArticlesResource, ArticleResource
from resources.author_resource import AuthorsResource, AuthorResource

from utils.database import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)


api.add_resource(ArticleResource, '/article/<string:title>')
api.add_resource(ArticlesResource, '/articles')
api.add_resource(AuthorResource, '/author/<string:name>')
api.add_resource(AuthorsResource, '/authors')

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=5000, debug=True)
