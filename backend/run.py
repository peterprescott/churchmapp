#!/usr/bin/env python 

from flask import Flask, request, render_template, jsonify 
from flaskext.markdown import Markdown
from flask_restful import Api, Resource, abort
from flask_cors import CORS
from werkzeug.security import safe_str_cmp
from passlib.hash import pbkdf2_sha256
from datetime import datetime, timedelta
import python_jwt as jwt, jwcrypto.jwk as jwk

from resources import TodoListResource, TodoResource, ConverterResource, GitRefresh, PlaceResource, PlaceListResource
from resources import JWT_security_key
from models import User, Place
from db import session
from md_text import hello

JWT_security_key = jwk.JWK.generate(kty='RSA', size=2048)

app = Flask(__name__)
Markdown(app)
CORS(app)
api = Api(app)

### ReSTful API
api.add_resource(ConverterResource, '/convert/<string:postcode>', endpoint='coords')
api.add_resource(TodoListResource, '/todos', endpoint='todos')
api.add_resource(TodoResource, '/todos/<string:id>', endpoint='todo')
api.add_resource(GitRefresh, '/git')
# api.add_resource(PlaceListResource, '/places', endpoint='places')
# api.add_resource(PlaceResource, '/places/<string:id>', endpoint='place')

### user registration/authentication
@app.route('/auth', methods=['POST'])
def authenticate():
    try:
        email = request.json['email']
        password = request.json['password']

        user = session.query(User)\
                    .filter(User.email==email)\
                    .first()
        if user: # if user already exists...
            # ... authenticate password
            if not pbkdf2_sha256\
                    .verify(
                        password,
                        user.password_hash
                        ):
                return jsonify(
                    {'message':'Wrong password for that email'}
                    ), 401
            else:
                message = 'Authentication successful'

        else: # else create new password hash and user
            hash = pbkdf2_sha256.hash(password)
            user = User(email=email, password_hash=hash)
            session.add(user)
            session.commit()
            message = 'Registration successful'

        # everyone still here gets a token
        payload = { 'userid': user.id }
        token = jwt.generate_jwt(
            payload, JWT_security_key, 
            'PS256', timedelta(minutes=15))
        return jsonify({
            'message': message, 
            'JWT': token
                    }), 202

    except Exception as e:
        return jsonify({'error':str(e)[:100]}), 500

### JWT validation
@app.route('/places', methods=['POST'])
def post_place():
    
    # first validate JWT
    try:
        token = request.headers.get('JWT')
        header, claims = jwt.verify_jwt(token, JWT_security_key, ['PS256'])
        userid = claims['userid']
    except Exception as e:
        return jsonify({'message': 'Validation failed'}), 401
    
    # then generate new JWT
    payload = {'userid': userid}
    new_token = jwt.generate_jwt(
        payload, JWT_security_key, 
        'PS256', timedelta(minutes=15))

    # then add place
    try:
   
        place = Place(
                        postcode = request.json['postcode'],
                        latitude = request.json['latitude'],
                        longitude = request.json['longitude'],
                        name = request.json['name'],
                        userid = userid
                    )
        session.add(place)
        session.commit()
        message = 'Token validation successful and place added.'

        return jsonify({'id': place.id,
                        'message': message,
                        'JWT': new_token}), 202
    
    except Exception as e:
        return jsonify({'message': 'JWT validation successful, but adding place failed.',
                        'error': str(e),
                       'JWT': new_token}), 417

@app.route('/places', methods=['GET'])
def get_users_places():
    
    # first validate JWT
    try:
        token = request.headers.get('JWT')
        header, claims = jwt.verify_jwt(token, JWT_security_key, ['PS256'])
        userid = claims['userid']
    except Exception as e:
        return jsonify({'message': 'Validation failed'}), 401
    
    # then generate new JWT
    payload = {'userid': userid}
    new_token = jwt.generate_jwt(
        payload, JWT_security_key, 
        'PS256', timedelta(minutes=15))
 
    # then get places
    try:
        places = session.query(Place).filter(Place.userid==userid).all()
        message = f'Token validation successful; found details of {len(places)} places for you.'
        place_list = []
        for place in places:
            place_list.append(
                {'id': place.id,
                 'postcode' : place.postcode,
                'latitude' : place.latitude,
                'longitude' : place.longitude,
                'name' : place.name}
                
            )

        return jsonify({'message': message,
                        'places': place_list,
                        'JWT': new_token}), 202
    
    except Exception as e:
        return jsonify({'message': 'JWT validation successful, but getting places failed.',
                        'error': str(e),
                       'JWT': new_token}), 417

@app.route('/places/<string:id>', methods=['DELETE'])
def delete_place(id):
    
    # first validate JWT
    try:
        token = request.headers.get('JWT')
        header, claims = jwt.verify_jwt(token, JWT_security_key, ['PS256'])
        userid = claims['userid']
    except Exception as e:
        return jsonify({'message': 'Validation failed'}), 401
    
   
    # then delete the specified place
    try:
        place = session.query(Place).filter(Place.id == id).first()
        assert place.userid == userid
        session.delete(place)
        session.commit()
        return {}, 204
    except Exception as e:
        return jsonify({'message': 
            f'JWT validation successful, but deleting place {id} failed. Does it exist?',
                        'error': str(e),
                       'JWT': new_token}), 417

### Cover page
@app.route('/')
def index():
    return render_template('frame.html', text=hello.md)


### Run directly
if __name__ == '__main__':
    app.run(debug=False)
