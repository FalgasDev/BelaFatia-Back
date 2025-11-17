from flask import Blueprint, request, jsonify
from errors import EmptyStringError, AuthError, IdNotExist
from models.cake_model import Cake
from config.database import db
from models.cake_model import registerCake, getCakes, getCakeById, updateCake, deleteCake

cake_blueprint = Blueprint('cake', __name__)

@cake_blueprint.route('/cakes', methods=['POST'])
def register_cake():
    data = request.json
    try:
        registerCake(data)
        return jsonify({'Message': 'Bolo cadastrado com sucesso.'}), 201
    except (EmptyStringError, AuthError, KeyError) as e:
        return jsonify({'Error': str(e)}), 400

@cake_blueprint.route('/cakes', methods=['GET'])
def get_cakes():
    return jsonify(getCakes())

@cake_blueprint.route('/cakes/<int:id>', methods=['GET'])
def get_cake_by_id(id):
    try:
        return jsonify(getCakeById())
    except IdNotExist as e:
        return jsonify({'Error': str(e)}), 404

@cake_blueprint.route('/cakes/<int:id>', methods=['PUT'])
def update_cake(id):
    data = request.json
    try:
        updateCake(id, data)
        return jsonify({'Message': 'Bolo atualizado com sucesso.'}), 200
    except IdNotExist as e:
        return jsonify({'Error': str(e)}), 404

@cake_blueprint.route('/cakes/<int:id>', methods=['DELETE'])
def delete_cake(id):
    try:
        deleteCake(id)
        return ('', 204)
    except IdNotExist as e:
        return jsonify({'Error': str(e)}), 404
