from flask import Flask, jsonify, request, render_template
from pydal import DAL
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import json

app = Flask(__name__)
app.config['DATABASE_URI'] = 'postgres://postgres:1234@db:5432/todo'
app.config['JWT_SECRET_KEY'] = 'servicekeyscreted'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_CSRF_IN_COOKIES'] = True
jwt = JWTManager(app)

db = DAL(app.config['DATABASE_URI'], folder="./migrations")


@app.route('/todos', methods=['GET'])
@jwt_required
def getTodos():
    db._adapter.reconnect()
    user = get_jwt_identity()
    todos = db(db.todo.user == user).select()
    return jsonify(todos=json.loads(todos.as_json()))

@app.route('/todos', methods=['POST', 'PUT', 'DELETE'])
@jwt_required
def todos():
    if not request.is_json:
        return jsonify(msg="Not JSON"), 404
    db._adapter.reconnect()
    todo = db.todo.insert(Desc=request.json.get('Desc', None), user=get_jwt_identity())
    todo = db(db.todo.id == todo).select().first()
    db.commit()
    return jsonify(todo=json.loads(todo.as_json()))


if __name__ == '__main__':
    from models import *
    app.run(host="0.0.0.0", port=5002)
