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

### user registration
@app.route('/register', methods=['POST'])
def register():
    try:
        email = request.json['email']
        password = request.json['password']
        hash = pbkdf2_sha256.hash(password)
        new_user = User(email=email, password_hash=hash)
        session.add(new_user)
        session.commit()
    except Exception as e:
        return jsonify({'error':str(e)[:62]}), 500

    return jsonify({'message':'User registered successfully'}), 201

### user authentication
@app.route('/auth', methods=['POST'])
def authenticate():
    try:
        email = request.json['email']
        password = request.json['password']
        user = session.query(User).filter(User.email==email).first()
        if user:
            if pbkdf2_sha256.verify(password,user.password_hash):
                payload = { 'email': email }
                token = jwt.generate_jwt(
                    payload, JWT_security_key, 
                    'PS256', timedelta(minutes=15))
                return jsonify({
                    'message': 'Authentication successful', 
                    'JWT': token
                            }), 202

    except Exception as e:
        return jsonify({'error':str(e)}), 500

### JWT validation
@app.route('/validate', methods=['POST'])
def validate():
    try:
        token = request.headers.get('JWT')
        header, claims = jwt.verify_jwt(token, JWT_security_key, ['PS256'])
        email = claims['email']
        return jsonify({'email': email})
    except Exception as e:
        return jsonify({'error':str(e)}), 500

### Cover page
@app.route('/')
def index():
    return render_template('frame.html', text=hello.md)


### Run directly
if __name__ == '__main__':
    app.run(debug=False)
