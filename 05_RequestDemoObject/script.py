from flask import Flask, request, render_template

app = Flask("__main__")

@app.route("/queryDemo")
def query_demo():
    # print(request.args)
    # return "<h1>Requests arguments printed to console.</h1>"
    # return render_template("queryDemo.html", args=request.args)
    return "Language entered is : {}".format(request.args.get("language"))

@app.route("/takeData")
def take_data():
    return render_template("take_data.html")

if __name__ == "__main__":
    app.run(debug=True)