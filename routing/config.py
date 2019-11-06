import simplejson
import json

from flask import Blueprint, request


def config_routing():
    config_bp = Blueprint('config', __name__)

    @config_bp.route('/config', methods=['GET'])
    def get_config():
        return load_json()

    @config_bp.route('/config', methods=['PUT'])
    def update_config():
        data = json.dumps(request.json)

        with open("weatherstation.json", "w") as json_file:
            json_file.write(data)
            json_file.flush()
            json_file.close()

        return load_json()

    def load_json():
        with open("weatherstation.json", "r") as json_file:
            data = json.load(json_file)
            print(json.dumps(data))
            return json.dumps(data)

    return config_bp


