from flask_restful import Resource
from flask import request
from db_connection import *


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