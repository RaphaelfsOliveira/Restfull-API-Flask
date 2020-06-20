from db_connection import *


class User:
    
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    
    @classmethod
    def find_by_username(cls, username):
        user = None

        query = "SELECT * FROM users WHERE username=?"
        result = db_manage(select_query, query, username)
        if result: user = cls(*result)
        
        return user
    
    @classmethod
    def find_by_id(cls, _id):
        user = None

        query = "SELECT * FROM users WHERE id=?"
        result = db_manage(select_query, query, _id)
        if result: user = cls(*result)
        
        return user
    
    @classmethod
    def delete(cls, _id):
        try:
            query = "DELETE FROM users WHERE id=?"
            db_manage(make_query, query, _id)
            return True
        except Exception as error:
            raise error