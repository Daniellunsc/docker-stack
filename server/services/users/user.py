from flask import Flask, jsonify, request
from pydal import DAL
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies
)

app = Flask(__name__)
app.config['DATABASE_URI'] = 'postgres://postgres:1234@localhost:5432/users'
app.config['JWT_SECRET_KEY'] = 'servicekeyscreted'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
jwt = JWTManager(app)
db = DAL(app.config['DATABASE_URI'], folder="services/users/migrations")
from models import *

@app.route('/')
def home():
    return jsonify(msg="HELLO FROM USERS SERVICES")

@app.route('/auth', methods=['POST'])
def auth():
    db._adapter.reconnect()
    if not request.is_json:
        return jsonify(msg="Not JSON"), 404
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = db((db.users.username == username)&(db.users.password == password)).select().first()
    if user:
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        resp = jsonify(token=access_token)
        set_access_cookies(resp, access_token)
        set_refresh_cookies(resp, refresh_token)
        return resp, 200
    else:
        return jsonify(msg="Not a user"), 404
    

@app.route('/users/register', methods=['POST'])
def user_req():
    db._adapter.reconnect()
    user = db.users.insert(username="Daniel", password="1234")
    db.commit()
    return jsonify(msg="ok", user=user)


if __name__ == '__main__':
    app.run(threaded=True, host="0.0.0.0", port=5001, debug=True)
