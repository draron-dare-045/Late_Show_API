from . import db

class Guest(db.Model):
    __tablename__ = 'guests'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(100), nullable=False)
    
    # Relationships
    appearances = db.relationship('Appearance', backref='guest', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'occupation': self.occupation
        }
    
    def __repr__(self):
        return f'<Guest {self.name}>'