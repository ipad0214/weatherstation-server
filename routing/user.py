import simplejson

from flask import Blueprint, request
from entities.user import User

def user_routing(session):
    user_bp = Blueprint('user', __name__)

    @user_bp.route('/user', methods=['GET'])
    def get_user():
        id = request.args.get('id')
        if id is None:
            return get_all_entries()
        else: 
            dataSet = session.query(User).filter(User.id == id).first()
            if dataSet is None:
                return {}

            return simplejson.dumps(dataSet.serialize, indent=2)

    @user_bp.route('/user', methods=['POST'])
    def post_user():
        new_user = User(
            name=request.json["name"],
            password=request.json["password"],
            granted=request.json["granted"],
            role=request.json["role"]
        )
        session.add(new_user)
        session.commit()

        return get_all_entries()

    @user_bp.route('/user', methods=['DELETE'])
    def delete_user():
        id = request.args.get('id');
        dataSet = session.query(User).filter(User.id == id).first()
        if dataSet is None:
            return get_all_entries()
        
        session.delete(dataSet)
        session.commit()

        return get_all_entries()

    @user_bp.route('/user', methods=['PATCH'])
    def update_user():
        id = request.args.get('id');
        dataSet = session.query(User).filter(User.id == id).first()
        if dataSet is None:
            return get_all_entries()

        dataSet.name=request.json["name"],
        dataSet.password=request.json["password"],
        dataSet.granted=request.json["granted"],
        dataSet.role=request.json["role"]
        session.commit()

        return get_all_entries()


    def get_all_entries():
        return simplejson.dumps([user.serialize for user in session.query(User)], indent=2)

    return user_bp

