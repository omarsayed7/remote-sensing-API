from flask import request, send_file
from flask_restplus import Namespace, Resource, fields
from application import db
from application.entities import Contact

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
    'Description': fields.String(
        required=True,
        description="Inquirer's Message"
    )
})


@namespace.route('')
class ContactUs(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.response(201, 'Created')
    @namespace.expect(contact_us)
    # @namespace.marshal_with(segmentation_model, code=201, description='Object created')
    def post(self):
        '''Post method for segmentation of an given lat/long bounding box'''
        data = request.json
        firstName = data['FirstName']
        lastName = data['LastName']
        name =  firstName + " " + lastName
        email = data['Email']
        description = data['Description']
        new_contact_info = Contact(name, email, description)
        db.session.add(new_contact_info)
        db.session.commit()
        return {'message': "Created!"}, 201