import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, redirect

import views

app = Flask(__name__)
load_dotenv()

# URL ROUTING
app.add_url_rule('/', view_func=views.home)

if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))
