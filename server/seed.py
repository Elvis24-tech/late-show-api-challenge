from app import create_app
from models.user import User
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance
from werkzeug.security import generate_password_hash
from models import db

def seed_data():
    app = create_app()
    with app.app_context():
        Appearance.query.delete()
        Episode.query.delete()
        Guest.query.delete()
        User.query.delete()
        
        user1 = User(username='admin', password_hash=generate_password_hash('password123'))
        db.session.add(user1)
        
        guest1 = Guest(name='John Doe', occupation='Actor')
        guest2 = Guest(name='Jane Smith', occupation='Comedian')
        db.session.add_all([guest1, guest2])
        
        episode1 = Episode(date='2025-06-01', number=101)
        episode2 = Episode(date='2025-06-02', number=102)
        db.session.add_all([episode1, episode2])
        
        appearance1 = Appearance(rating=4, guest_id=1, episode_id=1)
        appearance2 = Appearance(rating=5, guest_id=2, episode_id=2)
        db.session.add_all([appearance1, appearance2])
        
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()