#!/usr/bin/python3
from app.models.Base_models import BaseModel
from flask_sqlalchemy import SQLAlchemy
from app import db

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()

        if not name or len(name) > 50:
            raise ValueError("Name must be between 1 and 50 characters")

        self.name = name

db = SQLAlchemy()

class Amenity(db.Model):
    __tablename__ = 'amenities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
