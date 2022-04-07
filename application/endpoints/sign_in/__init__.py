from flask import request, Response, send_file, jsonify
from flask_restplus import Namespace, Resource, fields
from application import db
from application.entities import User

namespace = Namespace('sign-in', 'Getting sign-in data')

sign_in = namespace.model('Sign_In', {
    'Username': fields.String(
        required=True,
        description="Account's Username"
    ),
    'Password': fields.String(
        required=True,
        description="Account's Password"
    )
})


@namespace.route('')
class Sign_In(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.response(201, 'Created')
    @namespace.expect(sign_in)
    # @namespace.marshal_with(segmentation_model, code=201, description='Object created')
    def post(self):
        data = request.json
        username = data['Username']
        password = data['Password']
        user = User.query.filter(User.userName == username).first().query.filter(User.password == password).first()
        if user:
            return {'message': "Created!"}, 201
        else:
            return {"message": "User not found"}, 404