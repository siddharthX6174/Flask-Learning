from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask("__main__")

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Postgres%40123@localhost:5432/flask_database' # %40 -> @
# app.config['SQLALCHEMY_DATABASE_URT'] = 'postgresql://username:password@localhost/dbname'  # Intentional typo for demonstration

db = SQLAlchemy(app)

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False)
    done = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

@app.route('/addTask')
def add_task():
    return render_template('add_task.html')

@app.route('/saveTask', methods=['POST'])
def save_task():
    title = request.form.get('task_title')
    if not title:
        return "Task title is required", 400

    new_task = Task(title=title)
    db.session.add(new_task)
    db.session.commit()
    return "Task saved successfully!"


@app.route("/getTasks", methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return render_template("tasks.html", tasks=tasks)

# update task to done
@app.route('/updateTask', methods=['GET', 'POST'])
def update_task_page():
    if request.method == 'POST':
        task_id = request.form.get('task_id')
        task = Task.query.get(task_id)

        if not task:
            return "Task not found", 404

        task.done = True
        db.session.commit()
        return redirect(url_for('update_task_page'))

    tasks = Task.query.all()
    return render_template("update_task.html", tasks=tasks)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)