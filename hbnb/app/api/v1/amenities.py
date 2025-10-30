#!/usr/bin/python3
from flask_restx import Namespace, Resource, fields
from flask import jsonify, request
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

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
            api.abort(400, 'Invalid input data.')
        try:
            new_amenity = facade.create_amenity(data)
            return jsonify({'id': new_amenity.id, 'name': new_amenity.name}), 201
        except ValueError as e:
            api.abort(400, str(e))

    @api.response(200, 'List of amenities retrieved successfully.')
    def get(self):
        """Retrieve a list of all Amenities"""
        amenities = facade.get_all_amenities()
        result = [{'id': a.id, 'name': a.name} for a in amenities]
        return jsonify(result)


@api.route('/<string:amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully.')
    @api.response(404, 'Amenity not found.')
    def get(self, amenity_id):
        """Get amenity detail by id"""
        try:
            amenity = facade.get_amenity(amenity_id)
            return jsonify({'id': amenity.id, 'name': amenity.name})
        except ValueError:
            api.abort(404, 'Amenity not found.')

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully.')
    @api.response(404, 'Amenity not found.')
    @api.response(400, 'Invalid input data.')
    def put(self, amenity_id):
        """Update an existing Amenity"""
        data = api.payload
        if not data or 'name' not in data:
            api.abort(400, 'Invalid input data.')
        try:
            updated_amenity = facade.update_amenity(amenity_id, data)
            return {'message': 'Amenity updated successfully'}, 200
        except ValueError as e:
            api.abort(400, str(e))
        except KeyError:
            api.abort(404, 'Amenity not found.')
