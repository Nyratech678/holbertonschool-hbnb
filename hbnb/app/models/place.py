#!/usr/bin/python3
from app.models.Base_models import BaseModel
from app.models.user import User
from flask_sqlalchemy import SQLAlchemy
from app import db

db = SQLAlchemy()

class Place(BaseModel):
    def __init__(self, title, description="", price_by_night=0.0, latitude=0.0, longitude=0.0, owner=None):
        super().__init__()

        if not title or len(title) > 100:
            raise ValueError("Title must be between 1 and 100 characters.")
        if description and len(description) > 500:
            raise ValueError("Description max 500 characters.")
        if price_by_night <= 0:
            raise ValueError("Price must be positive.")
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude must be between -90.0 and 90.0.")
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude must be between -180.0 and 180.0.")
        if not isinstance(owner, User):
            raise ValueError("Owner must be an instance of User.")

        self.title = title
        self.description = description
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    __tablename__ = 'places'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(256), nullable=True)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    reviews = db.relationship('Review', backref='place', lazy=True)
    amenities = db.relationship('Amenity', secondary=place_amenity,
    lazy='subquery', backref=db.backref('places', lazy=True))
    place_amenity = db.Table('place_amenity',
    db.Column('place_id', db.Integer, db.ForeignKey('places.id'), primary_key=True),
    db.Column('amenity_id', db.Integer, db.ForeignKey('amenities.id'), primary_key=True)
)
