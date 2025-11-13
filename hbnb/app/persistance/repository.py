#!/usr/bin/python3
from abc import ABC, abstractmethod
from app import db

class Repository(ABC):
    """Abstract base class for repository pattern"""
    
    @abstractmethod
    def add(self, obj):
        pass
    
    @abstractmethod
    def get(self, obj_id):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def update(self, obj_id, data):
        pass
    
    @abstractmethod
    def delete(self, obj_id):
        pass
    
    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass


class SQLAlchemyRepository(Repository):
    """SQLAlchemy implementation of Repository pattern"""
    
    def __init__(self, model):
        self.model = model
    
    def add(self, obj):
        """Add a new object to the database"""
        db.session.add(obj)
        db.session.commit()
        return obj

    def get(self, obj_id):
        """Get an object by ID"""
        return self.model.query.get(obj_id)
    
    def get_all(self):
        """Get all objects"""
        return self.model.query.all()
    
    def update(self, obj_id, data):
        """Update an object with new data"""
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                if hasattr(obj, key) and key not in ['id', 'created_at']:
                    setattr(obj, key, value)
            db.session.commit()
            return obj
        return None

    def delete(self, obj_id):
        """Delete an object by ID"""
        obj = self.get(obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()
            return True
        return False

    def get_by_attribute(self, attr_name, attr_value):
        """Get first object matching an attribute value"""
        return self.model.query.filter(getattr(self.model, attr_name) == attr_value).first()
