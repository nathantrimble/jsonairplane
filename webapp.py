import json
from flask import Flask, url_for, render_template, request, url_for

app = Flask(__name__)



@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/airport")
def render_airportdata():

    return render_template('airportdata.html')


@app.route('/airportresponse')
def render_aresponse():
    with open('airlines.json') as airlines:
        adata = json.load(airlines)

    chosenap = request.args['aps']
    choseyear = request.args['years']
    chosemonth = request.args['months']
    airlAmount = 0
    airlNames = ""
    totFlights = 0
    for a in adata:
        if a["Airport"]["Code"] == chosenap and a['Time']['Year'] == choseyear and a['Time']['Month'] == chosemonth:
            airlAmount = a['Statistics']['Carriers']["Total"]
            airlNames = a['Statistics']['Carriers']["Names"]
            totFlight = a['Statistics']["Flights"]['Total']
        return airlNames
        return airlAmount
        return totFlight
    return render_aresponse('airportresponse.html')





@app.route("/delay")
def render_delaydata():
    return render_template('delaydata.html')



if __name__=="__main__":
    app.run(debug=False)
