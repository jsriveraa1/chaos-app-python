import os

from flask import (
    Flask,
    Response,
    jsonify
)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def health_check():
    resp = Response()
    resp.status_code = 200
    return jsonify({'status': 'alive!'})