from flask import request, Response, send_file, jsonify
from flask_restplus import Namespace, Resource, fields
import sqlite3
from sqlite3 import Error

def userLogin(db_file,user_data):
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
        user_data = []
        username = data['Username']
        password = data['Password']
        user_data.append(username)
        user_data.append(password)

        return {'message': "Created!"}, 201

    def get(self):
        return send_file('utilis/tmp/thematic_layer.jpg', as_attachment=True, attachment_filename='thematic_layer.jpg', mimetype='image/jpeg')
