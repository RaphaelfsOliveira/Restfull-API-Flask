from werkzeug.security import safe_str_cmp
from resources.user import User


def authenticate(username, password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user
    
    return {'message': 'user not found'}, 404

def identity(payload):
    user_id = payload['identity']
    if user_id:
        return User.find_by_id(user_id)
    
    return {'message': 'user not found'}, 404