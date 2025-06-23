from server import create_app
from server.models import db, User, Guest, Episode, Appearance
from datetime import datetime

app = create_app()

with app.app_context():
    # Clear data
    db.drop_all()
    db.create_all()
    
    # Create users
    user1 = User(username='admin')
    user1.set_password('password')
    db.session.add(user1)
    
    # Create guests
    guests = [
        Guest(name='John Doe', occupation='Actor'),
        Guest(name='Jane Smith', occupation='Musician'),
        Guest(name='Bob Johnson', occupation='Comedian')
    ]
    db.session.add_all(guests)
    
    # Create episodes
    episodes = [
        Episode(date=datetime(2023, 1, 1), number=101),
        Episode(date=datetime(2023, 1, 2), number=102),
        Episode(date=datetime(2023, 1, 3), number=103)
    ]
    db.session.add_all(episodes)
    
    # Create appearances
    appearances = [
        Appearance(rating=4, guest_id=1, episode_id=1),
        Appearance(rating=5, guest_id=2, episode_id=1),
        Appearance(rating=3, guest_id=3, episode_id=2),
        Appearance(rating=5, guest_id=1, episode_id=3)
    ]
    db.session.add_all(appearances)
    
    db.session.commit()
    print("Seeded!")