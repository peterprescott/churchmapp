#!/usr/bin/env python

from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
import git

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

@app.route('/git', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('https://github.com/peterprescott/flask-vue-app')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

@app.route('/test')
def test_python_anywhere():
    # try again
    return 'success'

if __name__ == '__main__':
    app.run(debug=True)
