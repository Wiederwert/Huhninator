from flask import Flask, render_template
from flask_restful import Api, Resource
from random import choice
import os

basedir = os.getcwd()

with open(basedir + '/Huhninator/cites.txt', 'r') as cfile:
    cites = [
        {'id': i,
        'text': t} for i, t
        in enumerate(cfile.read().split('\n'))
    ]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


api = Api(app)

class Cites(Resource):
    def get(self):
        return choice(cites)

api.add_resource(Cites, '/cites')

if __name__ == '__main__':
    app.run(debug=True)