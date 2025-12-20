from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from models import  db, login,UserModel, CategoryMaster, BlogModel, BlogComment

app = Flask("__main__")
app.secret_key = 'ItshouldbeLongEnough'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Postgres%40123@localhost:5432/blog_db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login.init_app(app)

login.login_view = 'login'

@app.before_first_request
def create_all():
    db.create_all()




if __name__ == "__main__":
    app.run(debug=True)