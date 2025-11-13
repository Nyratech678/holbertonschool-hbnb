#!/usr/bin/python3
from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('amenities', description='Amenity operations')

# Initialize facade
facade = HBnBFacade()

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='The amenity name')
})


@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created.')
    @api.response(400, 'Invalid input data.')
    def post(self):
        """Register a new Amenity"""
        data = api.payload
        if not data or 'name' not in data:
            return {'error': 'Invalid input data.'}, 400
        try:
            new_amenity = facade.create_amenity(data)
            return {'id': new_amenity.id, 'name': new_amenity.name}, 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.response(200, 'List of amenities retrieved successfully.')
    def get(self):
        """Retrieve a list of all Amenities"""
        amenities = facade.get_all_amenities()
        result = [{'id': a.id, 'name': a.name} for a in amenities]
        return result, 200


@api.route('/<string:amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully.')
    @api.response(404, 'Amenity not found.')
    def get(self, amenity_id):
        """Get amenity detail by id"""
        try:
            amenity = facade.get_amenity(amenity_id)
            return {'id': amenity.id, 'name': amenity.name}, 200
        except ValueError:
            return {'error': 'Amenity not found.'}, 404

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully.')
    @api.response(404, 'Amenity not found.')
    @api.response(400, 'Invalid input data.')
    def put(self, amenity_id):
        """Update an existing Amenity"""
        data = api.payload
        if not data or 'name' not in data:
            return {'error': 'Invalid input data.'}, 400
        try:
            updated_amenity = facade.update_amenity(amenity_id, data)
            if updated_amenity:
                return {'message': 'Amenity updated successfully'}, 200
            return {'error': 'Amenity not found.'}, 404
        except ValueError as e:
            return {'error': str(e)}, 400

