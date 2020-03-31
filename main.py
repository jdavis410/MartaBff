import datetime

from breezecard import getBreezeCardInfo
from stations import getArrivalsByStation


from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
def root():
    return "Hello World"

@app.route('/station/nearest')
def nearestStation():
    return "URL Not Ready", 404

@app.route('/station/<stationName>/table')
def station(stationName):
    return getArrivalsByStation(stationName)

@app.route('/breezecard/<cardnumber>')
def breezecard(cardnumber):
    return getBreezeCardInfo(cardnumber)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
