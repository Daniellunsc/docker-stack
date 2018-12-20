import os
from flask import Flask, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
import time

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>')
def catch_all(path):
    print("bateu aqui")
    return redirect('http://localhost:5001/'+path, code=307)

if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0", port=5000)