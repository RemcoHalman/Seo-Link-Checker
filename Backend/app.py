import json
import os

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource

load_dotenv()

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

api_path = "api/v1"

def statusChecker(url):
    urls = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    for link in soup.select('a'):
        urls.append(link.get('href'))
    filtered = list(filter(None, urls)) 
    filtered.sort()
    return filtered

class ApiStatus(Resource):
    def get(self):
        return {'status': "Api is up and running"}

class  GetUrl(Resource):
    def get(self, url, extension):
        try:
            url = f"https://www.{url}.{extension}"
            r = requests.get(url)
            urls = statusChecker(url)
            if json.JSONDecodeError:
                status = {'link': url, 'status_code': r.status_code, 'links': urls }
            else:
                status = {'link': url, 'status_code': r.status_code, 'response': r.json()}
            
            return status
        except json.JSONDecodeError:
            pass 

api.add_resource(ApiStatus, f'/{api_path}/')
api.add_resource(GetUrl, 
                f'/{api_path}/<string:url>/<string:extension>')



if __name__ == '__main__':
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"), debug=os.getenv("DEBUG"))
