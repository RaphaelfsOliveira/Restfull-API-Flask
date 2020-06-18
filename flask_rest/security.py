from werkzeug.security import safe_str_cmp
from user import User

users = [User(1, 'Rolf', '1234')]

username_mapping = {user.username: user for user in users}
userid_mapping = {user.id: user for user in users}

def authenticate(username, password):
    print(username_mapping)
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user
    
    return {'message': 'user not found'}, 404

def identity(payload):
    user_id = payload['identity']
    if user_id:
        return userid_mapping.get(user_id, None)
    
    return {'message': 'user not found'}, 404