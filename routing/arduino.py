import simplejson

from flask import Blueprint, request
from entities.arduino import Arduino


def arduino_routing(session):
    arduino_bp = Blueprint('arduino', __name__)

    @arduino_bp.route('/arduino', methods=['GET'])
    def get_arduino():
        id = request.args.get('id')
        if id is None:
            return get_all_entries()
        else:
            dataSet = session.query(Arduino).filter(Arduino.id == id).first()
            if dataSet is None:
                return {}
                
            return simplejson.dumps(dataSet.serialize, indent=2)

    @arduino_bp.route('/arduino', methods=['POST'])
    def create_arduino_entry():
        new_arduino = Arduino(
            name = request.json["name"],
            version = request.json["version"],
            location = request.json["location"],
            role = request.json["role"]
        )
        session.add(new_arduino)
        session.commit()

        return get_all_entries()

    @arduino_bp.route('/arduino', methods=['DELETE'])
    def delete_arduino_entry():
        id = request.args.get('id');
        dataSet = session.query(Arduino).filter(Arduino.id == id).first()
        if dataSet is None:
            return {}

        session.delete(dataSet)
        session.commit()

        return get_all_entries()

    def get_all_entries():
        return simplejson.dumps([arduino.serialize for arduino in session.query(Arduino)], indent=2)

    return arduino_bp




