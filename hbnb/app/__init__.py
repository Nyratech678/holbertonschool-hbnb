#!/usr/bin/python3
from flask import Flask
from flask_restx import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
jwt = JWTManager()
db = SQLAlchemy()

def create_app(config_name='development'):
    app = Flask(__name__)
    
    # Load configuration
    from app.config import config
    app.config.from_object(config[config_name])
    
    # Add JWT secret key if not present
    if 'JWT_SECRET_KEY' not in app.config:
        app.config['JWT_SECRET_KEY'] = app.config.get('SECRET_KEY', 'default_secret_key')
    
    # Initialize extensions
    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)
    
    # Initialize API
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1/')
    
    # Register blueprints/namespaces
    from app.api.v1 import auth, users, places, reviews, amenities
    api.add_namespace(auth.api, path='/api/v1/auth')
    api.add_namespace(users.api, path='/api/v1/users')
    api.add_namespace(places.api, path='/api/v1/places')
    api.add_namespace(reviews.api, path='/api/v1/reviews')
    api.add_namespace(amenities.api, path='/api/v1/amenities')
    
    return app
