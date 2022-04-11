from http.client import HTTPResponse
from socket import socket
from flask import request, Response, send_file, jsonify
from flask_restplus import Namespace, Resource, fields
from http import HTTPStatus
from numpy import require
from application.utilis.inference import inference, fake_img_resp
from application.utilis.mapbox_request import mapbox_request

namespace = Namespace('segmentation-upload', 'Segmentation Upload APIs')

segmentation_model = namespace.model('SegModel_upload', {
    'Algorithm': fields.String(
        required=True,
        description="Machine Learning Algorithm"
    ),
    'PostProcessing': fields.String(
        required=True,
        description="Choose from two options (download output thematic layer or show the thematic layer on the map"
    )
})


@namespace.route('')
class Segmentaion_Upload(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.response(201, 'Created')
    @namespace.expect(segmentation_model)
    # @namespace.marshal_with(segmentation_model, code=201, description='Object created')
    def post(self):
        '''Post method for segmentation of an given lat/long bounding box'''
        data = request.json
        algorithm = data['Algorithm']
        postProcessing = data['PostProcessing']
        prediction_img = inference(classifier=algorithm)
        return {'message': "Created!"}, 201

    def get(self):
        return send_file('utilis/tmp/thematic_layer.jpg', as_attachment=True, attachment_filename='thematic_layer.jpg', mimetype='image/jpeg')
