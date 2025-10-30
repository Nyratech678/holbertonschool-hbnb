from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
import requests
from hbnb.app.services import facade

api = Namespace('admin', description='Admin operations')

@api.route('/users/<user_id>')
class AdminUserResource(Resource):
    @jwt_required()
    def put(self, user_id):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        
        data = requests.json
        email = data.get('email')

        if email:
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email is already in use'}, 400
        
         # Logic to update user details, including email and password
         updated_user = facade.update_user(
             user_id,
             email=email,
             password=data.get('password'),
             first_name=data.get('first_name'),
             last_name=data.get('last_name')
         )
        
@api.route('/users/')
class AdminCreateUser(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        
        user_data = requests.json
        email = user_data.get('email')

        if facade.get_user_by_email(email):
            return {'error': 'Email already registered'}, 400

        # Logic to create a new user
        new_user = facade.create_user(
            email=email,
            password=user_data.get('password'),
            first_name=user_data.get('first_name'),
            last_name=user_data.get('last_name'),
            is_admin=user_data.get('is_admin', False)
        )

@api.route('/users/<user_id>')
class AdminUserModify(Resource):
    @jwt_required()
    def put(self, user_id):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        
        data = requests.json
        email = data.get('email')

        if email:
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email is already in use'}, 400
        
         # Logic to update user details, including email and password
         updated_user = facade.update_user(
             user_id,
             email=email,
             password=data.get('password'),
             first_name=data.get('first_name'),
             last_name=data.get('last_name')
         )
        
        return {'message': 'User updated successfully', 'user': updated_user.to_dict()}, 200
    
@api.route('/amenities/')
class AdminAmenityCreate(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        
        amenity_data = requests.json
        name = amenity_data.get('name')

        if facade.get_amenity_by_name(name):
            return {'error': 'Amenity already exists'}, 400

        # Logic to create a new amenity
        new_amenity = facade.create_amenity(name=name)

        return {'message': 'Amenity created successfully', 'amenity': new_amenity.to_dict()}, 201
    
@api.route('/amenities/<amenity_id>')
class AdminAmenityModify(Resource):
    @jwt_required()
    def put(self, amenity_id):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        
        # Logic to update an amenity
        data = requests.json
        name = data.get('name')
        updated_amenity = facade.update_amenity(amenity_id, name=name)

@api.route('/places/<place_id>')
class AdminPlaceModify(Resource):
    @jwt_required()
    def put(self, place_id):
        current_user = get_jwt_identity()

        is_admin = current_user.get('is_admin', False)
        user_id = current_user.get('id')

        place = facade.get_place(place_id)
        if not is_admin and place.owner_id != user_id:
            return {'error': 'Unauthorized action'}, 403
        
        # Logic to update the place
        data = requests.json
        updated_place = facade.update_place(
            place_id,
            name=data.get('name'),
            description=data.get('description'),
            price=data.get('price')
        )