from flask import request
from flask_restful import Resource
from models.item import Item


class ItemResource(Resource):

    def get(self, name):
        item = Item.search_name(name)
        if item:
            return item.to_json()
         
        return {'message': 'item not found'}, 404
    
    def delete(self, name):
        item = Item.search_name(name)
        if item:
            item.delete()
            return {'message': 'item delete'}

        return {'message': 'item not found'}, 404


class ItemListCreateUpdate(Resource):

    def get(self):
        items = Item._all()
        if items:
            return {
                'items': [item.to_json() for item in items],
                'count': len(items)
            }
        
        return {'message': "don't have items"}, 500
    
    def post(self):
        data = request.get_json()
        if data:
            if Item.search_name(data.get('name')):
                return {'message': 'An item with name {} already exists'.format(data['name'])}, 400
            
            item = Item(**data)
            item.save()
            return {'message': 'item created successfully'}, 201
        
        return {'message': 'item need some name and price'}, 500
    
    def put(self):
        data = request.get_json()
        if data:
            item = Item.search_name(data.get('name'))
            if item:
                item.price = data['price']
                item.save()
                return {'message': 'item updated'}
                
            item = Item(**data)
            item.save()
            return data, 201

        return {'message': 'item need some name and price'}, 500