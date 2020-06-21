from flask import request
from flask_restful import Resource
from models.store import Store


class StoreResourceArgs(Resource):

    def get(self, name):
        store = Store.search_name(name)
        if store:
            return store.json()
         
        return {'message': 'Store not found'}, 404
    
    def delete(self, name):
        store = Store.search_name(name)
        if store:
            store.delete()
            return {'message': 'store delete'}

        return {'message': 'store not found'}, 404


class StoreResource(Resource):

    def get(self):
        stores = Store._all()
        if stores:
            return {
                'stores': [store.json() for store in stores],
                'count': len(stores)
            }
        
        return {'message': "don't have stores"}, 500
    
    def post(self):
        data = request.get_json()
        if data:
            if Store.search_name(data.get('name')):
                return {'message': 'An store with name {} already exists'.format(data['name'])}, 400
            
            store = Store(**data)
            store.save()
            return {'message': 'store created successfully'}, 201
        
        return {'message': 'store need some name and price'}, 500
    
    def put(self):
        data = request.get_json()
        if data:
            store = Store.search_name(data.get('name'))
            if store:
                store.name = data['new_name']
                store.save()
                return {'message': 'store updated'}
                
            store = Store(data['name'])
            store.save()
            return data, 201

        return {'message': 'store need some name and price'}, 500