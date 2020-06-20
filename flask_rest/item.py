from flask import request
from flask_restful import Resource
from db_connection import *


def get_item(name):
    return next(filter(lambda key: key['name'] == name, items), None)


class Item:
    
    def __init__(self, _id, name, price):
        self.id = _id
        self.name = name
        self.price = price

    @classmethod
    def search_name(cls, name):
        item = None

        query = "SELECT * FROM items WHERE name=?"
        result = db_manage(select_query, query, name)
        if result: item = cls(*result)

        return item
    
    @classmethod
    def get_all(cls):
        items = None

        query = "SELECT * FROM items"
        result = db_manage(select_query_all, query)
        if result: items = [cls(*item) for item in result]
        
        return items
    
    @classmethod
    def create(cls, data):
        try:
            query = "INSERT INTO items VALUES (NULL, ?, ?)"
            db_manage(make_query, query, data['name'], data['price'])
            return True
        except Exception as error:
            raise error
    
    @classmethod
    def delete(cls, name):
        try:
            query = "DELETE FROM items WHERE name=?"
            db_manage(make_query, query, name)
            return True
        except Exception as error:
            raise error


class ItemResource(Resource):

    def get(self, name):
        item = Item.search_name(name)
        if item:
            return item.__dict__
         
        return {'message': 'item not found'}, 404
    
    def delete(self, name):
        if Item.delete(name):
            return {'message': 'item delete'}

        return {'message': 'item not found'}, 404


class ItemListCreateUpdate(Resource):

    def get(self):
        items = Item.get_all()
        if items:
            return {
                'items': [item.__dict__ for item in items],
                'count': len(items)
            }
        
        return {'message': "don't have items"}, 500
    
    def post(self):
        data = request.get_json()
        if data and Item.search_name(data.get('name')):
            return {'message': 'An item with name {} already exists'.format(data['name'])}, 400
            
            Item.create(data)
            return {'message': 'item created successfully'}, 201
        
        return {'message': 'item need some name and price'}, 500
    
    def put(self):
        data = request.get_json()
        if data:
            if get_item(data.get('name')):
                item.update(data)
                return data
                
            items.append(data)
            return data, 201

        return {'message': 'item need some name and price'}, 500