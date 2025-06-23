from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.episode import Episode
from server.models.appearance import Appearance
from server import db
from datetime import datetime

episode_bp = Blueprint('episodes', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{
        'id': ep.id,
        'date': ep.date.isoformat(),
        'number': ep.number
    } for ep in episodes]), 200

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = [{
        'id': app.id,
        'rating': app.rating,
        'guest_id': app.guest_id,
        'guest_name': app.guest.name
    } for app in episode.appearances]
    
    return jsonify({
        'id': episode.id,
        'date': episode.date.isoformat(),
        'number': episode.number,
        'appearances': appearances
    }), 200

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({'message': 'Episode deleted successfully'}), 200