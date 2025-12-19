from flask import Flask, request
from sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token, JWTManager

app = Flask("__main__")

app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Postgres%40123@localhost:5432/auth' 
db = SQLAlchemy(app)
api = Api(app)
jwt = JWTManager(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    
# createing the resoure for registration
class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        # Logic for user registration
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {"message": "Username and password are required"}, 400
        
        if User.query.filter_by(username=username).first():
            return {"message": "User already exists"}, 400
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User registered successfully"}, 201
    

# login resource
class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username, password=password).first()
        if user and user.password == password:
            access_token = create_access_token(identity={'username': user.id})
            return {"access_token": access_token}, 200
        
        return {"message": "Invalid credentials"}, 401

api.add_resource(UserRegistration, '/register')
api.add_resource(UserLogin, '/login')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)