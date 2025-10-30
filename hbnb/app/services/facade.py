#!/usr/bin/python3
from app.models.user import User
from hbnb.app.models.amenity import Amenity
import sqlalchemy
from app.persistence.repository import SQLAlchemyRepository
from app.services.repositories.user_repository import UserRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        user.hash_password(user_data['password'])
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_user_by_email(email)
    
    def get_all_users(self):
        return self.user_repository.get_all()

    def get_user(self, user_id):
        return self.user_repository.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def create_amenity(self, amenity_data):
        name = amenity_data.get('name')
        if not name or len(name) > 50:
            raise ValueError("Amenity name must be between 1 and 50 characters")
        amenity = Amenity(name)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            raise ValueError(f"Amenity not found with id {amenity_id}")
        return amenity

    def get_all_amenities(self):
        return list(self.amenity_repo.all())

    def update_amenity(self, amenity_id, update_data):
        amenity = self.get_amenity(amenity_id)
        name = update_data.get('name')
        if name:
            if len(name) > 50:
                raise ValueError("Amenity name must be between 1 and 50 characters")
            amenity.name = name
        self.amenity_repo.update(amenity)
        return amenity

    def create_place(self, place_data):
        #Placeholder for logic to create a place, including validation for price, latitude and longitude
        name = place_data.get('name')
        price_by_night = place_data.get('price_by_night')
        latitude = place_data.get('latitude')
        longitude = place_data.get('longitude')
        owner = place_data.get('owner')

    def get_place(self, place_id):
        # Placeholder for logic to retrieve a place by ID, including associated owner and amenities
        return self.place_repo.get(place_id)
    
    def get_all_places(self):
    # Placeholder for logic to retrieve all places
        return list(self.place_repo.all())

    def update_place(self, place_id, place_data):
    # Placeholder for logic to update a place
        place = self.get_place(place_id)
        # Update place attributes based on place_data
        self.place_repo.update(place)
        return place
    
    def create_review(self, review_data):
        # Placeholder for logic to create a review, including validation for user_id, place_id, and rating
        user_id = review_data.get('user_id')
        place_id = review_data.get('place_id')
        rating = review_data.get('rating')
        if not user_id or not place_id or rating is None:
            raise ValueError("user_id, place_id, and rating are required to create a review")

    def get_review(self, review_id):
        # Placeholder for logic to retrieve a review by ID
        return self.review_repo.get(review_id)
    
    def get_all_reviews(self):
        # Placeholder for logic to retrieve all reviews
        return list(self.review_repo.all())
    
    def get_reviews_by_place(self, place_id):
        # Placeholder for logic to retrieve all reviews for a specific place
        return [review for review in self.review_repo.all() if review.place_id == place_id]
    
    def update_review(self, review_id, review_data):
        # Placeholder for logic to update a review
        review = self.get_review(review_id)
        self.review_repo.update(review)
        return review
    
    def delete_review(self, review_id):
        # Placeholder for logic to delete a review
        review = self.get_review(review_id)
        self.review_repo.delete(review)

    