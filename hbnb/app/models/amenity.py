#!/usr/bin/python3
from app.models.Base_models import BaseModel
from app import db

class Amenity(BaseModel):
    """Amenity model for storing amenity information"""
    __tablename__ = 'amenities'
    
    name = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        if not name or len(name) > 50:
            raise ValueError("Name must be between 1 and 50 characters")
        self.name = name

    def to_dict(self):
        """Convert amenity to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

