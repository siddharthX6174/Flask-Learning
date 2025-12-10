from flask import Flask, render_template 

app = Flask("__main__")

@app.route("/staticdemo")
def static_demo():
    return render_template("staticdemo.html")

if __name__ == "__main__":
    app.run(debug=True)