#!/usr/bin/env python 

from flask import Flask, request, render_template, jsonify 
from flaskext.markdown import Markdown
from flask_restful import Api, Resource
from flask_cors import CORS
from werkzeug.security import safe_str_cmp
from passlib.hash import pbkdf2_sha256
from datetime import datetime, timedelta
import python_jwt as jwt, jwcrypto.jwk as jwk

from resources import TodoListResource, TodoResource, ConverterResource, GitRefresh, ChurchResource, ChurchListResource
from models import User
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
api.add_resource(ChurchListResource, '/churches', endpoint='churches')
api.add_resource(ChurchResource, '/churches/<string:id>', endpoint='church')

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
        payload = { 'email': email }
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
@app.route('/validate', methods=['POST'])
def validate():
    try:
        token = request.headers.get('JWT')
        header, claims = jwt.verify_jwt(token, JWT_security_key, ['PS256'])
        email = claims['email']
        payload = {'email': email}
        new_token = jwt.generate_jwt(
            payload, JWT_security_key, 
            'PS256', timedelta(minutes=15))
        message = 'Token validation successful'

        return jsonify({'message': message,
                        'JWT': new_token}), 202
    except Exception as e:
        return jsonify({'message': 'Validation failed'}), 401

### Cover page
@app.route('/')
def index():
    return render_template('frame.html', text=hello.md)


### Run directly
if __name__ == '__main__':
    app.run(debug=False)
