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

    choseap = request.args['aps']
    choseyear = int(request.args['years'])
    chosemonth = int(request.args['months'])
    airlAmount = 0
    airlNames = ""
    totFlights = 0
    for a in adata:
        if a["Airport"]["Code"] == choseap and a['Time']['Year'] == choseyear and a['Time']['Month'] == chosemonth:
            airlAmount = a['Statistics']['Carriers']["Total"]
            airlNames = a['Statistics']['Carriers']["Names"]
            totFlight = a['Statistics']["Flights"]['Total']

    return render_template('airportresponse.html', aA = airlAmount, aN = airlNames, tF = totFlights, cA = choseap, cY = choseyear, cM = chosemonth)





@app.route("/delay")
def render_delaydata():
    return render_template('delaydata.html')



if __name__=="__main__":
    app.run(debug=True)
