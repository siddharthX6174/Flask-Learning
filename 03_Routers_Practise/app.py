from flask import Flask, render_template
import datetime

app = Flask("__main__")

@app.route("/get-greeting")
def get_greeting():
    now = datetime.datetime.now()
    hour = now.hour
    if 5 <= hour < 12:
        greeting = render_template('GoodMorning.html', hour_now=hour)
    elif 12 <= hour < 17:
        greeting = render_template('GoodAfternoon.html', hour_now=hour)
    else:
        greeting = render_template('GoodEvening.html', hour_now=hour)
    return greeting


if __name__ == "__main__":
    app.run(debug=True)