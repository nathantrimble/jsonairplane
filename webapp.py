import json
from flask import Flask, url_for, render_template, request, url_for

app = Flask(__name__)



@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/airport")
def render_airportdata():
    return render_template('airportdata.html')

@app.route("/delay")
def render_delaydata():
    return render_template('delaydata.html')

def getairportdata():
    with open('airlines.json') as airlines:
        adata = json.load(airlines)

    chosenap = request.args['aps']
    airlAmount = 0
    airlNames = ""
    for a in adata:
        if a["Name"] == chosenap:
            airlAmount = a["Total"]
            airlNames = a["Names"]


if __name__=="__main__":
    app.run(debug=False)
