#!/usr/bin/python3
"""
Database initialization script
Creates all tables and adds sample data
"""
from app import create_app, db
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review

def init_db():
    """Initialize the database with tables"""
    app = create_app('development')
    
    with app.app_context():
        # Drop all tables and recreate them
        print("Dropping all tables...")
        db.drop_all()
        
        print("Creating all tables...")
        db.create_all()
        
        print("Database initialized successfully!")
        print(f"Database location: {app.config['SQLALCHEMY_DATABASE_URI']}")

def seed_data():
    """Add sample data to the database"""
    app = create_app('development')
    
    with app.app_context():
        print("Adding sample data...")
        
        # Create admin user
        admin = User(
            first_name='Admin',
            last_name='User',
            email='admin@hbnb.com',
            password='',
            is_admin=True
        )
        admin.hash_password('admin123')
        db.session.add(admin)
        
        # Create regular user
        user = User(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            password='',
            is_admin=False
        )
        user.hash_password('password123')
        db.session.add(user)
        
        db.session.commit()
        print(f"Created users: admin@hbnb.com (admin) and john.doe@example.com")
        
        # Create amenities
        wifi = Amenity(name='WiFi')
        pool = Amenity(name='Swimming Pool')
        parking = Amenity(name='Parking')
        db.session.add_all([wifi, pool, parking])
        db.session.commit()
        print(f"Created amenities: WiFi, Swimming Pool, Parking")
        
        # Create a place
        place = Place(
            title='Cozy Apartment',
            description='A beautiful apartment in the city center',
            price_by_night=100.0,
            latitude=40.7128,
            longitude=-74.0060,
            owner_id=user.id
        )
        place.amenities.append(wifi)
        place.amenities.append(parking)
        db.session.add(place)
        db.session.commit()
        print(f"Created place: {place.title}")
        
        # Create a review
        review = Review(
            text='Great place to stay!',
            rating=5,
            place_id=place.id,
            user_id=admin.id
        )
        db.session.add(review)
        db.session.commit()
        print(f"Created review for {place.title}")
        
        print("\nSample data added successfully!")
        print("\nTest credentials:")
        print("  Admin: admin@hbnb.com / admin123")
        print("  User: john.doe@example.com / password123")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'seed':
        init_db()
        seed_data()
    else:
        init_db()
