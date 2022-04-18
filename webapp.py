import json
from flask import Flask, url_for, render_template, request, url_for, Markup

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
    airpName = ''
    numCD = numLAD = numNASD = numSD = numWD = minCD = minLAD = minNASD = minSD = minWD = totD = totM = 0


    for a in adata:
        if a["Airport"]["Code"] == choseap and a['Time']['Year'] == choseyear and a['Time']['Month'] == chosemonth:
            airlAmount = a['Statistics']['Carriers']["Total"]
            airlNames = a['Statistics']['Carriers']["Names"]
            totFlights = a['Statistics']["Flights"]['Total']
            airpName = a['Airport']["Name"]
            numCD = a['Statistics']['# of Delays']["Carrier"]
            numLAD = a['Statistics']['# of Delays']["Late Aircraft"]
            numNASD = a['Statistics']['# of Delays']["National Aviation System"]
            numSD = a['Statistics']['# of Delays']["Security"]
            numWD = a['Statistics']['# of Delays']["Weather"]
            minCD = a['Statistics']['Minutes Delayed']['Carrier']
            minLAD = a['Statistics']['Minutes Delayed']['Late Aircraft']
            minNASD = a['Statistics']['Minutes Delayed']['National Aviation System']
            minSD = a['Statistics']['Minutes Delayed']['Security']
            minWD = a['Statistics']['Minutes Delayed']['Weather']
            totM = a['Statistics']['Minutes Delayed']['Total']
    totD = numCD + numLAD + numNASD + numSD + numWD
    return render_template('airportresponse.html', aA = airlAmount, aN = airlNames, tF = totFlights, cA = airpName, cY = choseyear, cM = chosemonth, nCD = numCD, nLAD = numLAD, nNASD = numNASD, nSD = numSD, nWD = numWD, mCD = minCD, mLAD = minLAD, mNASD = minNASD, mSD = minSD, mWD = minWD, tM = totM, tD = totD)

@app.route("/delay")
def render_delaydata():
    return render_template('delaydata.html')

@app.route("/delayresponse")
def render_dresponse():
    with open('airlines.json') as delayd:
        ddata = json.load(delayd)

    chosendelay = request.args['dlays']
    chosenairport = request.args['apz']
    delayammount = 0
    delaypoints = ""
    for d in ddata:
        for k in MAKE A LOO{ TO GO THRU DELAYS}
        if d['Statistics']['# of Delays'] == chosendelay and d["Airport"]["Code"] == chosenairport:
            delayamount = a['Statistics']['# of Delays'][chosendelay]
            delaypoints += Markup("{ x:"  + d['Time']['Label'] + ", y:" + d['Statistics']['# of Delays'][chosendelay] + "},")
    delaypoints = delaypoints[:-1]
    return render_template('delayresponse.html', cDL = chosendelay, dP = delaypoints)


if __name__=="__main__":
    app.run(debug=True)
