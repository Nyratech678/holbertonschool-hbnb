#!/usr/bin/python3
import re
from app.models.Base_models import BaseModel
import bcrypt
import uuid
from app import db, bcrypt

class User(BaseModel):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)

	first_name = db.Column(db.String(50), nullable=False)
	last_name = db.Column(db.String(50), nullable=False)
	email = db.Column(db.String(120), nullable=False, unique=True)
	password = db.Column(db.String(128), nullable=False)
	is_admin = db.Column(db.Boolean, default=False)
	places = db.relationship('Place', backref='user', lazy=True)
	reviews = db.relationship('Review', backref='user', lazy=True)

	def hash_password(self, password):
		"""Hashes the password before storing it."""
		self.password = bcrypt.generate_password_hash(password)

	def verify_password(self, password):
		"""Verifies if the provided password matches the hashed password."""
		return bcrypt.check_password_hash(self.password, password)



