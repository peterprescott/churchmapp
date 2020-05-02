#!/usr/bin/env python

from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

class Ping(Resource):
    def get(self):
        return 'pong'

api.add_resource(Ping, '/ping')

from resources import TodoListResource
from resources import TodoResource
from resources import ConverterResource

api.add_resource(ConverterResource, '/convert/<string:postcode>', endpoint='coords')
api.add_resource(TodoListResource, '/todos', endpoint='todos')
api.add_resource(TodoResource, '/todos/<string:id>', endpoint='todo')

if __name__ == '__main__':
    app.run(debug=True)
