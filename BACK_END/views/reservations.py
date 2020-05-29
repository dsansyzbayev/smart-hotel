from flask import Blueprint, jsonify, request
from db.models import Reservation
from mongoengine import NotUniqueError

reservations = Blueprint('reservations', __name__)


@reservations.route('/reservations/', methods=['POST'])
def create_hotel():
    body = request.get_json()
    try:
        hotel = Reservation(**body).save()
        hotel_id = hotel.id
    except:
        return {'error': 'This reservation is already in database!'}
    return {'id': str(hotel_id)}, 200


@reservations.route('/reservations/', methods=['GET'])
def get_all_hotels():
    all_hotels = Reservation.objects.all()
    return jsonify(all_hotels)


@reservations.route('/reservations/<id>/', methods=['GET'])
def get_hotel_by_id(id):
    try:
        hotel = Reservation.objects.get(pk=id)
        return jsonify(hotel)
    except:
        return jsonify({'error': 'Reservation does not exist'})


@reservations.route('/reservations/<id>/', methods=['PUT'])
def update_hotel(id):
    body = request.get_json(force=True)
    Reservation.objects.get(pk=id).update(**body)
    return '', 200


@reservations.route('/reservations/<id>/', methods=['DELETE'])
def delete_hotel(id):
    Reservation.objects.get(pk=id).delete()
    return '', 200
