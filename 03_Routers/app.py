from flask import Flask

app = Flask("__main__")

@app.route("/myhome")
def home():
    return "Welcome to the Home Page!"

# creating a dynamic route
@app.route("/blog/<int:blog_no>")
def get_blog(blog_no):
    msg = f"This is blog number {blog_no}."
    return msg

# @app.route("/home")
# @app.route("/home/<username>")
# def dynamic_home(username="Guest"):
#     msg = f"Welcome to the home page of {username}!"
#     return msg
# app.add_url_rule("/home", "dynamic_home_default", dynamic_home)
# app.add_url_rule("/home/<username>", "dynamic_home_user", dynamic_home)# url, endpoint, view Function

@app.route("/yourhome", defaults={"username": "Guest"})
@app.route("/yourhome/<username>")
def dynamic_home(username):
    return f"Welcome to the home page of {username}!"



def blog():
    msg = "These are all blogs."
    return msg
app.add_url_rule("/get_blogs", "blog", blog) # url, endpoint, view Function


@app.route("/check_odd_even/<int:number>")
def check_odd_even(number):
    if number % 2 == 0:
        return f"The number {number} is <b>Even</b><hr>."
    else:
        return f"The number {number} is <b>Odd</b>."

if __name__ == "__main__":
    app.run(debug=True)