from flask import Flask
from flask.templating import render_template

app = Flask("__main__")

@app.route('/printTable/<int:number>')
def print_table(number):
    return render_template('table.html', num=number)

if __name__ == "__main__":
    app.run(debug=True)