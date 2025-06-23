from flask import Blueprint, request, jsonify
from server.models.guest import Guest
from server import db

guest_bp = Blueprint('guests', __name__)

@guest_bp.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([{'id': guest.id, 'name': guest.name, 'occupation': guest.occupation} for guest in guests]), 200