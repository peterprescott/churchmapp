
from models import Todo, Converter
from db import session

from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with
import git
import os.path


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

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)

class ConverterResource(Resource):
    @marshal_with(converter_fields)
    def get(self, postcode):
        coords = session.query(Converter).filter(Converter.postcode == postcode).first()
        if not coords:
            abort(404, message=f"{postcode} does not appear to be a valid postcode.")
        return coords

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


class Ping(Resource):
    def get(self):
        return 'pong!'


class GitRefresh(Resource):
    def post(self):
        repo = git.Repo(os.path.join('~','flask-vue-app'))
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
