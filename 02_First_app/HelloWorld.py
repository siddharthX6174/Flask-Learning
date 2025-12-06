from flask import Flask

app = Flask(__name__) # create flaskk app object/instance

@app.route('/hello') # route decorator

def helloworld():
    msg = "Hello Guest !!!!, Welcome to our journey of Flask Web betchi."
    return msg


# agar flask run karna hai to neeche wali lines uncomment kar do
if __name__ == '__main__':
    app.run(port=5001,debug=True) # run the flask app