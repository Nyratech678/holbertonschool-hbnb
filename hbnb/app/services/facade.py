#!/usr/bin/python3
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from app.persistance.repository import SQLAlchemyRepository
from app import db

class HBnBFacade:
    def __init__(self):
        self.user_repo = SQLAlchemyRepository(User)
        self.amenity_repo = SQLAlchemyRepository(Amenity)
        self.place_repo = SQLAlchemyRepository(Place)
        self.review_repo = SQLAlchemyRepository(Review)

    # User methods
    def create_user(self, user_data):
        """Create a new user with hashed password"""
        user = User(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            email=user_data['email'],
            password='',  # Temporary, will be hashed
            is_admin=user_data.get('is_admin', False)
        )
        user.hash_password(user_data['password'])
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """Get user by ID"""
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """Get user by email"""
        return self.user_repo.get_by_attribute('email', email)
    
    def get_all_users(self):
        """Get all users"""
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        """Update user information"""
        return self.user_repo.update(user_id, user_data)

    # Amenity methods
    def create_amenity(self, amenity_data):
        """Create a new amenity"""
        name = amenity_data.get('name')
        if not name or len(name) > 50:
            raise ValueError("Amenity name must be between 1 and 50 characters")
        amenity = Amenity(name=name)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        """Get amenity by ID"""
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            raise ValueError(f"Amenity not found with id {amenity_id}")
        return amenity

    def get_all_amenities(self):
        """Get all amenities"""
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, update_data):
        """Update amenity information"""
        name = update_data.get('name')
        if name and len(name) > 50:
            raise ValueError("Amenity name must be between 1 and 50 characters")
        return self.amenity_repo.update(amenity_id, update_data)

    # Place methods
    def create_place(self, place_data):
        """Create a new place"""
        place = Place(
            title=place_data['title'],
            description=place_data.get('description', ''),
            price_by_night=place_data['price_by_night'],
            latitude=place_data.get('latitude', 0.0),
            longitude=place_data.get('longitude', 0.0),
            owner_id=place_data['owner_id']
        )
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        """Get place by ID"""
        return self.place_repo.get(place_id)
    
    def get_all_places(self):
        """Get all places"""
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        """Update place information"""
        return self.place_repo.update(place_id, place_data)

    def delete_place(self, place_id):
        """Delete a place"""
        return self.place_repo.delete(place_id)
    
    # Review methods
    def create_review(self, review_data):
        """Create a new review"""
        review = Review(
            text=review_data['text'],
            rating=review_data['rating'],
            place_id=review_data['place_id'],
            user_id=review_data['user_id']
        )
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        """Get review by ID"""
        return self.review_repo.get(review_id)
    
    def get_all_reviews(self):
        """Get all reviews"""
        return self.review_repo.get_all()
    
    def get_reviews_by_place(self, place_id):
        """Get all reviews for a specific place"""
        return [review for review in self.review_repo.get_all() if review.place_id == place_id]
    
    def update_review(self, review_id, review_data):
        """Update review information"""
        return self.review_repo.update(review_id, review_data)
    
    def delete_review(self, review_id):
        """Delete a review"""
        return self.review_repo.delete(review_id)


    