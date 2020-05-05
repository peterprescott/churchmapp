#!/usr/bin/env python

from flask import Flask, request, render_template
from flaskext.markdown import Markdown
from md_text import hello
from flask_restful import Api, Resource
from flask_cors import CORS

from resources import TodoListResource, TodoResource, ConverterResource, GitRefresh, ChurchResource, ChurchListResource


app = Flask(__name__)
Markdown(app)
CORS(app)
api = Api(app)


api.add_resource(ConverterResource, '/convert/<string:postcode>', endpoint='coords')
api.add_resource(TodoListResource, '/todos', endpoint='todos')
api.add_resource(TodoResource, '/todos/<string:id>', endpoint='todo')
api.add_resource(GitRefresh, '/git')
api.add_resource(ChurchListResource, '/churches', endpoint='churches')
api.add_resource(ChurchResource, '/church/<string:id>', endpoint='church')

@app.route('/')
def index():
    return render_template('frame.html', text=hello.md)

if __name__ == '__main__':
    app.run(debug=True)
