#!/usr/bin/python3
from app.models.Base_models import BaseModel
from app.models.associations import place_amenity
from app import db

class Place(BaseModel):
    """Place model for storing place information"""
    __tablename__ = 'places'
    
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    price_by_night = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    owner_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    
    # Relationships
    reviews = db.relationship('Review', backref='place', lazy=True, cascade='all, delete-orphan')
    amenities = db.relationship('Amenity', secondary=place_amenity, lazy='subquery',
                               backref=db.backref('places', lazy=True))

    def __init__(self, title, price_by_night, owner_id, description="", latitude=0.0, longitude=0.0, **kwargs):
        super().__init__(**kwargs)
        
        if not title or len(title) > 100:
            raise ValueError("Title must be between 1 and 100 characters.")
        if description and len(description) > 500:
            raise ValueError("Description max 500 characters.")
        if price_by_night <= 0:
            raise ValueError("Price must be positive.")
        if latitude and not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude must be between -90.0 and 90.0.")
        if longitude and not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude must be between -180.0 and 180.0.")

        self.title = title
        self.description = description
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id

    def to_dict(self):
        """Convert place to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price_by_night': self.price_by_night,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

