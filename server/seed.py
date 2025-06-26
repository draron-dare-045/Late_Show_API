from datetime import date
from server.app import create_app
from server.models import db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

def seed_data():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        
        user1 = User(username='admin')
        user1.set_password('password')
        db.session.add(user1)
        
        
        guests = [
            Guest(name='Tom Hanks', occupation='Actor'),
            Guest(name='Serena Williams', occupation='Tennis Player'),
            Guest(name='Elon Musk', occupation='Entrepreneur'),
            Guest(name='Oprah Winfrey', occupation='Media Mogul'),
            Guest(name='Stephen King', occupation='Author')
        ]
        db.session.add_all(guests)
        
        
        episodes = [
            Episode(date=date(2024, 1, 15), number=1001),
            Episode(date=date(2024, 1, 16), number=1002),
            Episode(date=date(2024, 1, 17), number=1003),
            Episode(date=date(2024, 1, 18), number=1004),
            Episode(date=date(2024, 1, 19), number=1005)
        ]
        db.session.add_all(episodes)
        
        db.session.commit()
        
        
        appearances = [
            Appearance(rating=5, guest=guests[0], episode=episodes[0]),
            Appearance(rating=4, guest=guests[1], episode=episodes[0]),
            Appearance(rating=5, guest=guests[2], episode=episodes[1]),
            Appearance(rating=3, guest=guests[3], episode=episodes[2]),
            Appearance(rating=4, guest=guests[4], episode=episodes[3]),
            Appearance(rating=5, guest=guests[0], episode=episodes[4])
        ]
        db.session.add_all(appearances)
        
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()
