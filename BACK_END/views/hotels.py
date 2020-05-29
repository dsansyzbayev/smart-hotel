from flask import  Blueprint, jsonify, request
from db.models import Hotel
from mongoengine import NotUniqueError

hotels = Blueprint('hotels', __name__)


@hotels.route('/hotels/', methods=['POST'])
def create_hotel():
    body = request.get_json()
    try:
        hotel = Hotel(**body).save()
        hotel_id = hotel.id
    except NotUniqueError:
        return {'error':'This hotel is already in the database!'}
    return {'id': str(hotel_id)}, 200


@hotels.route('/hotels/', methods=['GET'])
def get_all_hotels():
    all_hotels = Hotel.objects.all()
    return jsonify(all_hotels)


@hotels.route('/hotels/<id>/', methods=['GET'])
def get_hotel_by_id(id):
    try:
        hotel = Hotel.objects.get(pk=id)
        return jsonify(hotel)
    except:
        return jsonify({'error': 'Hotel does not exist!'})


@hotels.route('/hotels/<id>/', methods=['PUT'])
def update_hotel(id):
    body = request.get_json(force=True)
    Hotel.objects.get(pk=id).update(**body)
    return '',200


@hotels.route('/hotels/<id>/', methods=['DELETE'])
def delete_hotel(id):
    Hotel.objects.get(pk=id).delete()
    return '', 200
