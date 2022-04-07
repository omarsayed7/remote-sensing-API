from flask import request
from flask_restplus import Namespace, Resource, fields
# from application import db
# from application.models import User

namespace = Namespace('sign-up', 'Getting sign-up data')

sign_up = namespace.model('Sign_Up', {
    'FirstName': fields.String(
        required=True,
        description="Account's First Name"
    ),
    'LastName': fields.String(
        required=True,
        description="Account's Last Name"
    ),
    'Username': fields.String(
        required=True,
        description="Account's Username"
    ),
    'Email': fields.String(
        required=True,
        description="Account's E-mail"
    ),
    'Password': fields.String(
        required=True,
        description="Account's Password"
    )
})


@namespace.route('')
class Sign_Up(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.response(201, 'Created')
    @namespace.expect(sign_up)
    # @namespace.marshal_with(segmentation_model, code=201, description='Object created')
    def post(self):
        data = request.json
        firstname = data['FirstName']
        lastname = data['LastName']
        name = firstname + " " + lastname
        username = data['Username']
        email = data['Email']
        password = data['Password']
        print(name, username, email, password)
        # print(User.query.all())
        # new_user = User(name, username, email, password)
        # db.session.add(new_user)
        # db.session.commit()
        return {'message': "Created!"}, 201
