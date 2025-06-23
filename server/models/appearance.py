from server import db

class Appearance(db.Model):
    __tablename__ = 'appearances'
    
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    
    def __repr__(self):
        return f'<Appearance {self.id}>'
    
    def validate_rating(self):
        if not 1 <= self.rating <= 5:
            raise ValueError('Rating must be between 1 and 5')