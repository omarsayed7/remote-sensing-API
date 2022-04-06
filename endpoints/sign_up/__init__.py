from flask import request, Response, send_file, jsonify
from flask_restplus import Namespace, Resource, fields
import sqlite3
from sqlite3 import Error


def newUser(db_file,user_data):
    """ create a database connection to a SQLite database """
    db = None
    try:
        db = sqlite3.connect(db_file)
        cursor = db.cursor()
        sql_create ='''CREATE TABLE IF NOT EXISTS USERS(
                FIRST_NAME CHAR(20) NOT NULL,
                LAST_NAME CHAR(20) NOT NULL,
                USERNAME CHAR(20) NOT NULL,
                EMAIL CHAR(50) NOT NULL,
                PASSWORD CHAR(20) NOT NULL
                )'''
        sql =''' INSERT INTO USERS(FIRST_NAME,LAST_NAME,USERNAME,EMAIL,PASSWORD)
              VALUES(?,?,?,?,?) '''
        cursor.execute(sql_create)
        cursor.execute(sql,user_data)
        db.commit()

    except Error as e:
        print(e)
    finally:
        if db:
            db.close()



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
        user_data=[]
        firstname = data['FirstName']
        lastname = data['LastName']
        username = data['Username']
        email = data['Email']
        password = data['Password']
        user_data.append(firstname)
        user_data.append(lastname,)
        user_data.append(username)
        user_data.append(email)
        user_data.append(password)
        newUser("utilis/database/users.db",user_data)
        return {'message': "Created!"}, 201

    def get(self):
        return send_file('utilis/tmp/thematic_layer.jpg', as_attachment=True, attachment_filename='thematic_layer.jpg', mimetype='image/jpeg')
