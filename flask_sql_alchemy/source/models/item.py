from db_connection import *


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
    def insert(cls, price, _id):
        try:
            query = "UPDATE items SET price=? WHERE id=?"
            db_manage(make_query, query, price, _id)
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