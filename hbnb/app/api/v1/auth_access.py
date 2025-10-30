from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('places', description='Place operations')

@api.route('/')
class PlaceList(Resource):
    @jwt_required()
    def post(self):
        """Create a new place"""
        current_user = get_jwt_identity()
        # Logic to create a new place for the logged-in user
        return {"message": f"Place created by user {current_user}"}, 201
    
@api.route('/<place_id>')
class PlaceResource(Resource):
    @jwt_required()
    def put(self, place_id):
        current_user = get_jwt_identity()
        place = facade.get_place(place_id)
        if place.owner_id != current_user:
            return {'error': 'Unauthorized access'}, 403
        # Logic to update the place
        return {"message": f"Place {place_id} updated by user {current_user}"}, 200
    
    