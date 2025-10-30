#!/usr/bin/python3
from app.models.Base_models import BaseModel
from app.models.place import Place
from app.models.user import User
from flask_sqlalchemy import SQLAlchemy
from app import db

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()

        if not text or not text.strip():
            raise ValueError("Text cannot be empty.")
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            raise ValueError("Rating must be an integer between 1 and 5.")
        if not isinstance(place, Place):
            raise ValueError("Place must be an instance of Place.")
        if not isinstance(user, User):
            raise ValueError("User must be an instance of User.")

        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

db = SQLAlchemy()

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer, db.ForeignKey('places.id'), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(256), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
