from flask_restful import Resource
from flask import request
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


class UserRegister(Resource):
    
    def post(self):
        data = request.get_json()
        if data:
            if User.find_by_username(data['username']):
                return {'message': 'The user {} already exists'.format(data['username'])}, 400

            query = "INSERT INTO users VALUES (NULL, ?, ?)"
            db_manage(make_query, query, data['username'], data['password'])

            return {'message': 'user created successfully'}, 201    
        
        return {'message': 'need user and password'}, 500


class UserResource(Resource):

    def get(self):
        query = "SELECT * FROM users"
        result = db_manage(select_query_all, query)
        if result:
            users = [{'id': user[0], 'name': user[1], 'password': user[2]} for user in result]
            return {'users': users, 'count': len(users)}
        
        return {'message': "don't have users"}, 500

class UserGetDelete(Resource):

    def delete(self, _id):
        if User.delete(_id):
            return {'message': 'user deleted'}
        
        return {'message': 'user not found'}, 404