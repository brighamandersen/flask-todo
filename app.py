from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

if os.environ.get('FLASK_DEBUG') == '1':
    app.config['DEBUG'] = True
else:
    app.config['DEBUG'] = False

# database

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# models

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    complete = db.Column(db.Boolean)


# urls / views

@app.route("/")
def index():
    todos = Todo.query.order_by(Todo.id.desc()).all()
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    contentToAdd = request.form["added-todo"]
    if contentToAdd:
        todo = Todo(content=contentToAdd, complete=False)
        db.session.add(todo)
        db.session.commit()
    return redirect(url_for("index"))


@app.route("/update/<id>", methods=["POST"])
def update(id):
    todo = Todo.query.get(id)
    todo.content = request.form["edited-content"]
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/complete/<id>")
def complete(id):
    todo = Todo.query.get(id)
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<id>")
def delete(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
