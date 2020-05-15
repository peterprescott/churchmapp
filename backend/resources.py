
from models import Todo, Converter, Place, User
from db import session

from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with
import git
import os.path
from passlib.hash import pbkdf2_sha256
import python_jwt as jwt, jwcrypto.jwk as jwk

JWT_security_key = jwk.JWK.generate(kty='RSA', size=2048)


todo_fields = {
    'id': fields.Integer,
    'task': fields.String,
    'uri': fields.Url('todo', absolute=True),
}

converter_fields = {
    'id': fields.Integer,
    'postcode': fields.String,
    'latitude': fields.Float,
    'longitude': fields.Float
}

place_fields = {
    'id': fields.Integer,
    'postcode': fields.String,
    'latitude': fields.Float,
    'longitude': fields.Float,
    'name': fields.String,
    'userid': fields.Integer,
    'uri': fields.Url('place', absolute=True),
}

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)
parser.add_argument('postcode', type=str)
parser.add_argument('latitude', type=float)
parser.add_argument('longitude', type=float)
parser.add_argument('name', type=str)
parser.add_argument('JWT', type=str, location='headers')


class TodoResource(Resource):
    @marshal_with(todo_fields)
    def get(self, id):
        todo = session.query(Todo).filter(Todo.id == id).first()
        if not todo:
            abort(404, message="Todo {} doesn't exist".format(id))
        return todo

    def delete(self, id):
        todo = session.query(Todo).filter(Todo.id == id).first()
        if not todo:
            abort(404, message="Todo {} doesn't exist".format(id))
        session.delete(todo)
        session.commit()
        return {}, 204

    @marshal_with(todo_fields)
    def put(self, id):
        parsed_args = parser.parse_args()
        todo = session.query(Todo).filter(Todo.id == id).first()
        todo.task = parsed_args['task']
        session.add(todo)
        session.commit()
        return todo, 201


class TodoListResource(Resource):
    @marshal_with(todo_fields)
    def get(self):
        todos = session.query(Todo).all()
        return todos

    @marshal_with(todo_fields)
    def post(self):
        parsed_args = parser.parse_args()
        todo = Todo(task=parsed_args['task'])
        session.add(todo)
        session.commit()
        return todo, 201


class PlaceResource(Resource):
    @marshal_with(place_fields)
    def get(self, id):
        place = session.query(Place).filter(Place.id==id).first()
        if not place:
            abort(404, message="Place {} is not in our database".format(id))
        return place 

    def delete(self, id):
        place = session.query(Place).filter(Place.id == id).first()
        if not place:
            abort(404, message="Place {} doesn't exist".format(id))
        session.delete(place)
        session.commit()
        return {}, 204

class PlaceListResource(Resource):
    @marshal_with(place_fields)
    def get(self):
        try:
            parsed_args = parser.parse_args()
            token = parsed_args['JWT']
            header, claims = jwt.verify_jwt(token, JWT_security_key, ['PS256'])
            userid = claims['userid']
            payload = {'userid': userid}
            new_token = jwt.generate_jwt(
                payload, JWT_security_key, 
                'PS256', timedelta(minutes=15))
            message = 'Token validation successful'

            places = session.query(Place).filter(Place.userid==userid).all()
            return places, 202
        except Exception as e:
            return 'validation failed', 401

        return places

    @marshal_with(place_fields)
    def post(self):
        parsed_args = parser.parse_args()

        place = Place(
            postcode=parsed_args['postcode'],
            latitude=parsed_args['latitude'], 
            longitude=parsed_args['longitude'], 
            name=parsed_args['name'], 
            userid=parsed_args['userid']
        )
        session.add(place)
        session.commit()
        return place, 201
### JWT validation
# @app.route('/validate', methods=['POST'])
# def validate():
#     try:
#         token = request.headers.get('JWT')
#         header, claims = jwt.verify_jwt(token, JWT_security_key, ['PS256'])
#         email = claims['email']
#         payload = {'email': email}
#         new_token = jwt.generate_jwt(
#             payload, JWT_security_key, 
#             'PS256', timedelta(minutes=15))
#         message = 'Token validation successful'

#         return jsonify({'message': message,
#                         'JWT': new_token}), 202
#     except Exception as e:
#         return jsonify({'message': 'Validation failed'}), 401


class ConverterResource(Resource):
    @marshal_with(converter_fields)
    def get(self, postcode):
        coords = session.query(Converter).filter(Converter.postcode == postcode).first()
        if not coords:
            abort(404, message=f"{postcode} does not appear to be a valid postcode.")
        return coords


class GitRefresh(Resource):
    def post(self):
        repo = git.Repo(os.path.join('~','churchmapp'))
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
