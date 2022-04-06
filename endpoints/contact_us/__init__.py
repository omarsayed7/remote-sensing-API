from flask import request, Response, send_file, jsonify
from flask_restplus import Namespace, Resource, fields
import sqlite3

namespace = Namespace('contact-us', 'Getting contact-us data')

contact_us = namespace.model('Contact_Us', {
    'FirstName': fields.String(
        required=True,
        description="Inquirer's First Name"
    ),
    'LastName': fields.String(
        required=True,
        description="Inquirer's Last Name"
    ),
    'Email': fields.String(
        required=True,
        description="Inquirer's E-mail"
    ),
    'Message': fields.String(
        required=True,
        description="Inquirer's Message"
    )
})


@namespace.route('')
class Contact_Us(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.response(201, 'Created')
    @namespace.expect(contact_us)
    # @namespace.marshal_with(segmentation_model, code=201, description='Object created')
    def post(self):
        '''Post method for segmentation of an given lat/long bounding box'''
        data = request.json
        firstName = data['FirstName']
        lastname = data['LastName']
        email = data['Email']
        msg = data['Message']
        return {'message': "Created!"}, 201

    def get(self):
        return send_file('utilis/tmp/thematic_layer.jpg', as_attachment=True, attachment_filename='thematic_layer.jpg', mimetype='image/jpeg')
