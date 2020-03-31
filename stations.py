from martapy import RailClient
from flask import jsonify

rail_client = RailClient(api_key="0e421e5c-b433-4c65-8203-5c9c1145e078")

#TODO: Add station Validation
def getArrivalsByStation(station):

    try:
        arrivals = rail_client.arrivals().by_station(station)

        arr = [{
        "to":arrival.destination,
        "when":arrival.waiting_time,
        "station":arrival.station,
        "line": arrival.line,
        "direction": arrival.direction,
        "trainId": arrival.train_id } for arrival in arrivals]
        return jsonify(arr), 200
    except:
        return "500 Server Error", 500
