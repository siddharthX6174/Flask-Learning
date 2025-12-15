from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route("/getProfile")
def get_profile():
    name = request.cookies.get('userID')
    if name is None:
        name = "Guest"
    return "Welcome {}".format(name)

@app.route("/login" , methods=["GET", "POST"])
def login():

    if request.method == "POST":
        res = make_response(render_template("get_profile.html"))
        res.set_cookie("userID", request.form["username"])
        return res

    return '''<form method="POST" action="/login"> 
    <p><h3>Enter your name </h3></p>
    <p><input type="text" name="username"></p>
    <p><input type="submit" value="GO"></p>
    </form>'''

@app.route("/logout")
def logout():
    res = make_response(render_template("get_profile.html"))
    res.delete_cookie("userID")
    return res

if __name__ == "__main__":
    app.run(debug=True)