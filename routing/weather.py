import simplejson

from flask import Blueprint, request
from entities.weather import Weather
from datetime import datetime


def weather_routing(session):
    pressure_bp = Blueprint('weather', __name__)

    @pressure_bp.route('/weather', methods=['GET'])
    def get_rain():
        return get_all_entrys()

    @pressure_bp.route('/weather', methods=['POST'])
    def create_pressure_entry():
        new_weather = Weather(
            pressure=request.json["pressure"],
            altitude=request.json["altitude"],
            realAltitude=request.json["realAltitude"],
            sealevel=request.json["sealevel"],
            temperature=request.json["temperature"],
            humidity=request.json["humidity"],
            date=create_time_stamp()
        )
        session.add(new_weather)
        session.commit()

        return get_all_entrys()

    def get_all_entrys():
        return simplejson.dumps([weather.serialize for weather in session.query(Weather)], indent=2)

    def create_time_stamp():
        return datetime.now()

    return pressure_bp




