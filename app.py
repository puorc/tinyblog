#! usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_graphql import GraphQLView
from models.main import session
from flask_cors import CORS
from schema import schema

app = Flask(__name__)
CORS(app)
app.debug = True

app.add_url_rule('/graphql',
                 view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True, context={'session': session}))


@app.route('/')
def index():
    return "Go to /graphql"

if __name__ == "__main__":
    app.run()
