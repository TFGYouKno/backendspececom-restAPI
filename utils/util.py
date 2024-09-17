import jwt
from datetime import datetime, timedelta, timezone
from functools import wraps #wraps is a decorator that copies the metadata of the passed in function to the wrapper function
from flask import request, jsonify

SECRET_KEY = 'sooper_seekrit'

def encode_token(user_id):
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(hours=1), #setting expiration time to 1 hour
        'iat': datetime.now(timezone.utc), #setting the time the token was issued
        'sub': user_id #setting the subject of the token to the user_id
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256' )
    return token

def token_required(f): #f is the function that the decorator is wrapping
    @wraps(f)
    def wrapper(*args, **kwargs): #when wrapping around function we need to make sure its parameters make it through the wrapper
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split()[1]
                payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')
                print("Payload", payload)
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Token has expired'}), 401 #unauthenticated
            except jwt.InvalidTokenError:
                return jsonify({'message': 'Invalid token'}), 401 #not a valid token
            return f(*args, **kwargs) #if the token is valid, run the function
        else:
            return jsonify({'message': 'Token is missing'}), 401
    return wrapper

def user_validation(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split()[1]
                payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')
                print("Payload", payload)
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Token has expired'}), 401
            except jwt.InvalidTokenError:
                return jsonify({'message': 'Invalid token'}), 401
            return f(token_id=payload['sub'], *args, **kwargs)
        else:
            return jsonify({'message': 'Token is missing'}), 401
        
    return wrapper
        
#==============for role based access control================
def encode_role_token(user_id, role_id):
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(hours=1), #setting expiration time to 1 hour
        'iat': datetime.now(timezone.utc), #setting the time the token was issued
        'sub': user_id, #setting the subject of the token to the user_id
        'admin': role_id
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256' )
    return token

def admin_required(f): #f is the function that the decorator is wrapping
    @wraps(f)
    def wrapper(*args, **kwargs): #when wrapping around function we need to make sure its parameters make it through the wrapper
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split()[1]
                payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')
                print("Payload", payload)
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Token has expired'}), 401 #unauthenticated
            except jwt.InvalidTokenError:
                return jsonify({'message': 'Invalid token'}), 401 #not a valid token
            if payload['admin'] == 1:
                return f(*args, **kwargs)
            else:
                return jsonify({'message': 'You are not authorized to access this resource'}), 401
            return f(*args, **kwargs) #if the token is valid, run the function
        else:
            return jsonify({'message': 'Token is missing'}), 401
    return wrapper