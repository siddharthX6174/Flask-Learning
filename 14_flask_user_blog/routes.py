from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for
from flask_login import login_required, current_user, login_user, logout_user
from models import  db, login,UserModel, CategoryMaster, BlogModel, BlogComment

app = Flask("__main__")
app.secret_key = 'ItshouldbeLongEnough'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Postgres%40123@localhost:5432/blog_db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login.init_app(app)

login.login_view = 'login'

# --------------------------------------------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
            #return redirect(url_for('blogs'))
            return "You are already logged in."
    if request.method == 'POST':
        email = request.form.get('email')
        user = UserModel.query.filter_by(email=email).first()
        if user is not None and user.check_password(request.form.get('password')):
            login_user(user)
            return "login successful"
    return render_template('login.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
            #return redirect(url_for('blogs'))
            return "You are already logged in."
    
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        if UserModel.query.filter_by(email=email).first():
            return "Email Already Exists."
        
        user = UserModel(email=email, username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        return "Thankyou"
    
    return render_template('register.html')

#----------------------------------------------------------------
# @app.before_first_request
# def create_all():
#     db.create_all()



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)