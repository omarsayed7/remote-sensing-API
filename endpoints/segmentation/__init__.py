from http.client import HTTPResponse
from socket import socket
from flask import request, Response
from flask_restplus import Namespace, Resource, fields
from http import HTTPStatus

from numpy import require

namespace = Namespace('segmentation-model', 'Segmentation APIs')

segmentation_model = namespace.model('SegModel', {
    'Bbox': fields.List(
        fields.Float,
        required=True,
        description="List of Lat/long bounding box(min point and max point)"
    ),
    'Algorithm': fields.String(
        required=True,
        description="Machine Learning Algorithm"
    ),
    'PostProcessing': fields.String(
        required=True,
        description="Choose from two options (download output mask or show the mask on the map"
    )
})


@namespace.route('')
class Segmentaion(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.expect(segmentation_model)
    @namespace.marshal_with(segmentation_model, code=HTTPStatus.CREATED)
    def post(self):
        '''Post method for segmentation of an given lat/long bounding box'''
        data = request.json
        bbox = data['Bbox']
        algorithm = data['Algorithm']
        postProcessing = data['PostProcessing']

        return Response("{'a':'b'}", status=200, mimetype='application/json')
