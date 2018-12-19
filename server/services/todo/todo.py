from flask import Flask, jsonify, request
from pydal import DAL
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import json

app = Flask(__name__)
app.config['DATABASE_URI'] = 'postgres://postgres:1234@localhost:5432/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JWT_SECRET_KEY'] = 'servicekeyscreted'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
jwt = JWTManager(app)

db = DAL(app.config['DATABASE_URI'], folder="services/todo/migrations")
from models import *

@app.route('/')
@jwt_required
def home():
    return jsonify(msg="HELLO FROM TODO SERVICES")

@app.route('/getTodos', methods=['GET'])
@jwt_required
def getTodos():
    db._adapter.reconnect()
    user = get_jwt_identity()
    todos = db(db.todo.user == user).select()
    lt = []
    return jsonify(todos=json.loads(todos.as_json()))

@app.route('/todos', methods=['POST'])
@jwt_required
def todos():
    if not request.is_json:
        return jsonify(msg="Not JSON"), 404
    
    db._adapter.reconnect()
    todo = db.todo.insert(Desc=request.json.get('Desc', None), user=get_jwt_identity())
    db.commit()
    return jsonify(user=todo)


if __name__ == '__main__':
    app.run(threaded=True, host="0.0.0.0", port=5002, debug=True)
