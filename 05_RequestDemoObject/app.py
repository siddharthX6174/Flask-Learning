from flask import Flask, request

app = Flask("__main__")

@app.route("/requestDemo")
def request_demo():
    # print(request.__dict__.items())
    print(request.method)
    return "This page printed request object"


if __name__ == "__main__":
    app.run(debug=True)