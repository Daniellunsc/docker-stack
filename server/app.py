import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
import time

alembic = Alembic()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:1234@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
alembic.init_app(app)
db = SQLAlchemy(app)

@app.route('/checkin/<user>', methods=['POST'])
def checkin(user):
    users_seen[user] = time.strftime('%Y-%m-%d')
    return jsonify(success=True, user=user)

@app.route('/last-seen/<user>')
def lastseen(user):
    if user in users_seen:
        return jsonify(user=user, date=users_seen[user])
    else:
        return jsonify(error="Who?", user=user), 404

@app.route('/api/message')
def message():
    return jsonify(msg="ok")

if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0")