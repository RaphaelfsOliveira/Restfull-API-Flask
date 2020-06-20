from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from user import UserRegister, UserResource

app = Flask(__name__)
app.secret_key = 'password'
api = Api(app)

jwt = JWT(app, authenticate, identity)

if __name__ == "__main__": app.run(debug=True)

@app.route('/')
def home():
    return 'new api'


items = [
    {
        "name": "Book",
        "price": 4.34
    },
    {
        "name": "Desk",
        "price": 100.2
    },
    {
        "name": "Pen",
        "price": 3.2
    }
]

def get_item(name):
    return next(filter(lambda key: key['name'] == name, items), None)

class Item(Resource):

    def get(self, name=None):
        item = get_item(name)
        if item:
            return {'item': item}, 200
         
        return {'message': 'item not found'}, 404
    
    def delete(self, name):
        item = get_item(name)
        if item:
            items.remove(item)
            return {'message': 'item delete'}
        
        return {'message': 'item not found'}, 404


class ItemListCreateUpdate(Resource):

    # @jwt_required()
    def get(self):
        return {
            'items': items,
            'count': len(items)
        }
    
    def post(self):
        data = request.get_json()
        if data:
            if get_item(data['name']):
                return {'message': 'An item with name {} already exists'.format(data['name'])}, 400
            
            new_item = {
                'name': data['name'],
                'price': data['price']
            }
            items.append(new_item)

            return new_item, 201
        
        return {'message': 'item need some name and price'}, 500
    
    def put(self):
        data = request.get_json()
        if data:
            item = get_item(data['name'])
            if item:
                item.update(data)
                return data    
                
            items.append(data)
            return data, 201

        return {'message': 'item need some name and price'}, 500


api.add_resource(ItemListCreateUpdate, '/items')
api.add_resource(Item, '/items/<string:name>')
api.add_resource(UserRegister, '/register')
api.add_resource(UserResource, '/users')

