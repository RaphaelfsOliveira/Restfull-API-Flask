import sqlite3
from flask_restful import Resource
from flask import request
from db_connection import select_query, create_query, select_query_all


class User:
    
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    
    @classmethod
    def find_by_username(cls, username):
        user = None

        query = "SELECT * FROM users WHERE username=?"
        result = select_query(query, username)
        if result: user = cls(*result)
        
        return user
    
    @classmethod
    def find_by_id(cls, _id):
        user = None

        query = "SELECT * FROM users WHERE id=?"
        result = select_query(query, _id)
        if result: user = cls(*result)
        
        return user


class UserRegister(Resource):
    
    def post(self):
        data = request.get_json()
        if data:
            query = "INSERT INTO users VALUES (NULL, ?, ?)"
            create_query(query, data['username'], data['password'])
            
            return {'message': 'user created successfully'}, 201    
        
        return {'message': 'need user and password'}, 500


class UserResource(Resource):

    def get(self):
        query = "SELECT * FROM users"
        result = select_query_all(query)
        return result

        