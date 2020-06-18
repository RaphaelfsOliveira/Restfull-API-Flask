from flask import Flask, request
from flask_restful import Resource, Api

import datetime

app = Flask(__name__)
api = Api(app)

if __name__ == "__main__": app.run(debug=True)

@app.route('/')
def home():
    return 'new api'


items = []

class Item(Resource):
    
    def get(self, name=None):
        for item in items:
            if item['name'] == name:
                return item
        
        return {'message': 'item not found'}, 404
    
    def delete(self, name):
        for item in items:
            if item['name'] == name:
                items.remove(item)
                return {'message': 'item removed'}
        
        return {'message': 'item not found'}, 404


class ItemListCreateUpdate(Resource):
    
    def get(self):
        return {
            'items': items,
            'count': len(items)
        }
    
    def post(self):
        data = request.get_json()
        if data:
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
            for item in items:
                if data['name'] == item['name']:
                    item.update(data)
                    return data
                
            items.append(data)
            return data, 201

        return {'message': 'item need some name and price'}, 500


api.add_resource(ItemListCreateUpdate, '/items')
api.add_resource(Item, '/items/<string:name>')

