
from models import Todo, Converter, Church, User
from db import session
from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with
import git
import os.path
from passlib.hash import pbkdf2_sha256


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

church_fields = {
    'id': fields.Integer,
    'postcode': fields.String,
    'latitude': fields.Float,
    'longitude': fields.Float,
    'name': fields.String,
    'website': fields.String,
    'uri': fields.Url('church', absolute=True),
}

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)
parser.add_argument('postcode', type=str)
parser.add_argument('latitude', type=float)
parser.add_argument('longitude', type=float)
parser.add_argument('name', type=str)
parser.add_argument('user', type=str)


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


class ChurchResource(Resource):
    @marshal_with(church_fields)
    def get(self, id):
        church = session.query(Church).filter(Church.id==id).first()
        if not church:
            abort(404, message="Church {} is not in our database".format(id))
        return church

    def delete(self, id):
        church = session.query(Church).filter(Church.id == id).first()
        if not church:
            abort(404, message="Church {} doesn't exist".format(id))
        session.delete(church)
        session.commit()
        return {}, 204

    @marshal_with(church_fields)
    def put(self, id):
        parsed_args = parser.parse_args()
        church = session.query(Church).filter(Church.id == id).first()
        church.postcode=parsed_args['postcode'],
        church.name=parsed_args['name'],
        church.website=parsed_args['website'],
        church.latitude=parsed_args['latitude'],
        church.longitude=parsed_args['longitude'],
        session.add(church)
        session.commit()
        return church, 201


class ChurchListResource(Resource):
    @marshal_with(church_fields)
    def get(self):
        churches = session.query(Church).all()
        return churches

    @marshal_with(church_fields)
    def post(self):
        parsed_args = parser.parse_args()

        church = Church(postcode=parsed_args['postcode'],latitude=parsed_args['latitude'], longitude=parsed_args['longitude'], name=parsed_args['name'], user=parsed_args['user'])
        session.add(church)
        session.commit()
        return church, 201


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
