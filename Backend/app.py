import os
from dotenv import load_dotenv

from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api

load_dotenv()

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

API_PATH = "/api/v1"

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, f'{API_PATH}/')

if __name__ == '__main__':
    app.run(debug=os.getenv("DEBUG"))
