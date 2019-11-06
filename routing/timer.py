import simplejson

from flask import Blueprint, request
from entities.timer import Timer


def timer_routing(session):
    timer_bp = Blueprint('timer', __name__)

    @timer_bp.route('/timer', methods=['GET'])
    def get_rain():
        id = request.args.get('id')
        if id is None:
            return get_all_entries()
        else: 
            dataSet = session.query(Timer).filter(Timer.id == id).first()
            if dataSet is None:
                return {}
                
            return simplejson.dumps(dataSet.serialize, indent=2)

    @timer_bp.route('/timer', methods=['POST'])
    def create_pressure_entry():
        new_timer = Timer(
            name=request.json["name"],
            starttime=request.json["startTime"],
            duration=request.json["duration"],
        )
        session.add(new_timer)
        session.commit()

        all_entries = get_all_entries()
        return get_all_entries()

    @timer_bp.route('/timer', methods=['DELETE'])
    def delete_timer():
        id = request.args.get('id');
        dataSet = session.query(Timer).filter(Timer.id == id).first()
        if dataSet is None:
            return get_all_entries()
        
        session.delete(dataSet)
        session.commit()

        return get_all_entries()

    @timer_bp.route('/timer', methods=['PATCH'])
    def update_timer():
        id = request.args.get('id');
        dataSet = session.query(Timer).filter(Timer.id == id).first()
        if dataSet is None:
            return get_all_entries()

        dataSet.name = request.json['name']
        dataSet.startTime = request.json['startTime']
        dataSet.duration = request.json['duration']
        session.commit()

        return get_all_entries()


    def get_all_entries():
        return simplejson.dumps([timer.serialize for timer in session.query(Timer)], indent=2)

    return timer_bp




