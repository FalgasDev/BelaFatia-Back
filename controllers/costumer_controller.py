from errors import EmptyStringError, AuthError
from config.database import db
from models.costumer_model import register, login
from flask import Blueprint, request, jsonify

custumer_blueprint = Blueprint('custumer', __name__)

@custumer_blueprint.route('/register', methods=['POST'])
def register_customer():
    data = request.json
    try:
        register(data)
        return jsonify({'status': 'Success'}), 201

    except (KeyError, EmptyStringError, AuthError) as e:
        return jsonify({'Error': str(e)}), 400

@custumer_blueprint.route('/login', methods=['POST'])
def login_customer():
    data = request.json
    try:
        username = login(data)
        return jsonify({'username': username})
    except (KeyError, EmptyStringError, AuthError) as e:
        return jsonify({'Error': str(e)}), 400