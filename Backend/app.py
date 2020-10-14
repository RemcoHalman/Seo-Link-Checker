import os
from dotenv import load_dotenv
import requests

from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api

load_dotenv()

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

api_path = "api/v1"

class  GetUrl(Resource):
    def get(self, url):
        url = f"https://api.github.com/users/{url}"
        r = requests.get(url)
        status = {'link': url, 'status_code': r.status_code}
        # return r.json()
        return status

api.add_resource(GetUrl, 
                f'/{api_path}/GetUrl/',
                f'/{api_path}/GetUrl/<string:url>/')

if __name__ == '__main__':
    app.run(debug=os.getenv("DEBUG"))
