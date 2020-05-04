#!/usr/bin/env python

from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS

from resources import TodoListResource, TodoResource, ConverterResource, GitRefresh, Home


app = Flask(__name__)
# CORS(app)
api = Api(app)


api.add_resource(ConverterResource, '/convert/<string:postcode>', endpoint='coords')
api.add_resource(TodoListResource, '/todos', endpoint='todos')
api.add_resource(TodoResource, '/todos/<string:id>', endpoint='todo')
api.add_resource(GitRefresh, '/git')
api.add_resource(Home, '/home')


if __name__ == '__main__':
    app.run(debug=True)
