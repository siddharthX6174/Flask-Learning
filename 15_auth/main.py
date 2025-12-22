from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Postgres%40123@localhost:5432/auth_db01"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Database model
class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password_hash = db.Column(db.Text, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Routes
@app.route("/")
def index():
    if "username" in session:
        return redirect(url_for("dashboard"))
    return render_template("index.html")

# Login
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return render_template("index.html", error="Username and password required")

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        session["username"] = username
        return redirect(url_for("dashboard"))

    return render_template("index.html", error="Invalid credentials")

# Register
@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return render_template("index.html", error="Username and password required")

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return render_template("index.html", error="Username already exists")

    new_user = User(username=username)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    session["username"] = username
    return redirect(url_for("dashboard"))

# Dashboard
@app.route("/dashboard")
def dashboard():
    if "username" in session:
        return render_template("dashboard.html", username=session["username"])
    return redirect(url_for("index"))

# Logout
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
