import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:1234@172.18.0.2:5432/postgres'
app.config['SQLALCHEMY_TRACK_rMODIFICATIONS'] = True
db = SQLAlchemy(app)

with app.app_context():
    from models import *
    db.create_all()
@app.route('/')
def home():
    return jsonify(msg="KALLIU GAY")

@app.route('/api/message')
def message():
    return jsonify(msg="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0")