from flask import Flask, render_template

app = Flask("__main__")

@app.route('/filterDemo')
def filter_demo():
    names = ["Siddharth", "Saksham", "Mayank", "Samyak"]
    numbers = [100, 80, 60, 40]
    return render_template("filterDemo.html", context={"names": names, "numbers": numbers})

@app.route("/varDemo")
def var_demo():
    username = "Siddharth Chauhan"
    password = "secret"
    return render_template("varDemo.html", context={"username": username, "password": password})

if __name__ == "__main__":
    app.run(debug=True)