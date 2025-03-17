import os
import time
import random

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

@app.route('/operation', methods=['GET'])
def operation():

    time.sleep(random.randint(0,5))

    resp = Response()
    resp.status_code = 200
    return jsonify({'status': 'Completed!'})