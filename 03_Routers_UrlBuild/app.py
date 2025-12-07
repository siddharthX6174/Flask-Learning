from flask import Flask, url_for
app = Flask("__main__")

@app.route("/")
def index():
    return "This is index."

@app.route("/minehome")
@app.route("/minehome/<username>")
def dynamic_home(username="Guest"):
    msg = f"Welcome to the home page of {username}!"
    return msg

with app.test_request_context():
    print("URL for index():", app.url_for("index"))
    print("URL for dynamic_home():",url_for("dynamic_home"))
    print("URL for dynamic_home():",url_for("dynamic_home", username="siddharth"))
    print("URL for dynamic_home():",url_for("dynamic_home", username="siddharth chauhan", password="TopSecret"))

if __name__ == "__main__":
    app.run(debug=True)