import json
from flask import Flask, url_for, render_template, request, url_for

app = Flask(__name__)

with open('airlines.json') as airlines:
    airlines_data = json.load(airlines)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/airport")
def render_airportdata():
    return render_template('airportdata.html')

@app.route("/delay")
def render_delaydata():
    return render_template('delaydata.html')


if __name__=="__main__":
    app.run(debug=False)
