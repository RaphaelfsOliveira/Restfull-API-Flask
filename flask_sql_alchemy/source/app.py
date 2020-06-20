from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from resources.user import UserRegister, UserResource, UserGetDelete
from resources.item import ItemResource, ItemListCreateUpdate

app = Flask(__name__)
app.secret_key = 'password'

api = Api(app)
jwt = JWT(app, authenticate, identity)

api.add_resource(ItemListCreateUpdate, '/items')
api.add_resource(ItemResource, '/items/<string:name>')
api.add_resource(UserRegister, '/register')
api.add_resource(UserResource, '/users')
api.add_resource(UserGetDelete, '/users/<int:_id>')


@app.route('/')
def home():
    return 'api ok'

if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=5000, debug=True)
    