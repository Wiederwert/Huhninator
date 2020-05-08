from flask import Flask, render_template, jsonify
from flask_restful import Api, Resource
from random import choice
from cites import CITES

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


api = Api(app)

class Cites(Resource):
    def get(self):
        return choice(CITES)

api.add_resource(Cites, '/cites')

if __name__ == '__main__':
    app.run(debug=True)