from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from db import db

from security import authenticate, identity
from resources.user import UserRegister, UserResource, UserGetDelete
from resources.item import ItemResource, ItemListCreateUpdate
from resources.store import StoreResource, StoreResourceArgs

app = Flask(__name__)
app.secret_key = 'password'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def create_tables():
    db.create_all()

api = Api(app)
jwt = JWT(app, authenticate, identity)

api.add_resource(StoreResource, '/stores')
api.add_resource(StoreResourceArgs, '/stores/<string:name>')
api.add_resource(ItemListCreateUpdate, '/items')
api.add_resource(ItemResource, '/items/<string:name>')

api.add_resource(UserResource, '/users')
api.add_resource(UserRegister, '/register')
api.add_resource(UserGetDelete, '/users/<int:_id>')


@app.route('/')
def home():
    return 'api ok'

if __name__ == "__main__":
    db.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
    