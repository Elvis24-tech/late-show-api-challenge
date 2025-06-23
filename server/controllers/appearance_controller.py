from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.models.episode import Episode
from server import db

appearance_bp = Blueprint('appearances', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')
    
    if not all([rating, guest_id, episode_id]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    guest = Guest.query.get(guest_id)
    episode = Episode.query.get(episode_id)
    
    if not guest or not episode:
        return jsonify({'error': 'Guest or episode not found'}), 404
    
    try:
        appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
        appearance.validate_rating()
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
    db.session.add(appearance)
    db.session.commit()
    
    return jsonify({
        'id': appearance.id,
        'rating': appearance.rating,
        'guest_id': appearance.guest_id,
        'episode_id': appearance.episode_id
    }), 201