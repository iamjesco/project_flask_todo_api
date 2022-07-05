from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Suppress the flask dictionary keys sorting and forces to respect the defined schema order.
app.config['JSON_SORT_KEYS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


from models.database import Todos
from models.schemas import todo_schema, todos_schema


@app.route('/')
def home():
	return redirect(url_for('get_todos'))


@app.get('/api/todos/')
def get_todos():
	response = todos_schema.jsonify(Todos.query.all())
	return response, 200


@app.post('/api/todos/')
def add_todo():
	data = request.json
	payload = Todos(
		body=data.get('body'),
	)
	db.session.add(payload)
	db.session.commit()
	return todo_schema.jsonify(payload), 201
	

@app.get('/api/todos/<int:pk>')
def get_todo(pk):
	response = todo_schema.jsonify(Todos.query.get_or_404(pk))
	return response, 200


@app.patch('/api/todos/<int:pk>')
def update_todo(pk):
	payload = request.json
	query = Todos.query.get_or_404(pk)
	if 'body' in payload:
		query.body = payload.get('body')
	db.session.commit()
	return todo_schema.jsonify(query), 200


@app.delete('/api/todos/<int:pk>')
def delete_todo(pk):
	todo = Todos.query.get_or_404(pk)
	db.session.delete(todo)
	db.session.commit()
	return {}, 204


if __name__ == '__main__':
	app.run()
