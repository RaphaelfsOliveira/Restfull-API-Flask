from flask_restful import Resource
from flask import request
from models.user import User


class UserRegister(Resource):
    
    def post(self):
        data = request.get_json()
        if data:
            if User.find_by_username(data['username']):
                return {'message': 'The user {} already exists'.format(data['username'])}, 400

            user = User(**data)
            user.save()
            return {'message': 'user created successfully'}, 201    
        
        return {'message': 'need user and password'}, 500


class UserResource(Resource):

    def get(self):
        users = User._all()
        if users:
            return {
                'users': [user.json() for user in users],
                'count': len(users)
            }
        
        return {'message': "don't have users"}, 500

class UserGetDelete(Resource):

    def delete(self, _id):
        user = User.find_by_id(_id)
        if user:
            user.delete()
            return {'message': 'user deleted'}
        
        return {'message': 'user not found'}, 404