from flask import Flask, request, render_template

app = Flask("__main__")

@app.route("/")
def take_data():
    return render_template("takeData.html")

@app.route("/fetchData", methods=["POST"])
def fetch_data():
    print(request.form)
    return ("Request form is printed")
    # return render_template("fetchData.html", data=request.form)

if __name__ == "__main__":
    app.run(debug=True)