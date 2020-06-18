from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

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

class Item(Resource):
    
    def get(self, name=None):
        item = next(filter(lambda key: key['name'] == name, items), None)
        if item:
            return {'item': item}, 200
         
        return {'message': 'item not found'}, 404
    
    def delete(self, name):
        item = next(filter(lambda key: key['name'] == name, items), None)
        if item:
            items.remove(item)
            return {'message': 'item removed'}
        
        return {'message': 'item not found'}, 404


class ItemListCreateUpdate(Resource):

    @jwt_required()
    def get(self):
        return {
            'items': items,
            'count': len(items)
        }
    
    def post(self):
        data = request.get_json()
        if data:
            if next(filter(lambda key: key['name'] == data['name'], items), None):
                return {'message': 'An item with name {} already exists'.format(data['name'])}, 400

            items.append({
                'name': data['name'],
                'price': data['price']
            })
            return new_item, 201
        
        return {'message': 'item need some name and price'}, 500
    
    def put(self):
        data = request.get_json()
        if data:
            item = next(filter(lambda key: key['name'] == name, items), None)
            if item:
                item.update(data)
                return data    
                
            items.append(data)
            return data, 201

        return {'message': 'item need some name and price'}, 500


api.add_resource(ItemListCreateUpdate, '/items')
api.add_resource(Item, '/items/<string:name>')

