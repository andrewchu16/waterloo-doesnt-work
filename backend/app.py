from flask import Flask, request
from flask_cors import CORS
import json

from server import Server

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    app.run()


@app.route("/get_job", methods=["GET"])
def get_job():
    