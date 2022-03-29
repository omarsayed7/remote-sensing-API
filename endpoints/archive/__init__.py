from http.client import HTTPResponse
from socket import socket
from flask import request, Response, send_file, jsonify
from flask_restplus import Namespace, Resource, fields
from http import HTTPStatus
from numpy import require
from PIL import Image
from utilis.inference import inference, fake_img_resp
from utilis.mapbox_request import mapbox_request

namespace = Namespace('archive', 'Archived Images')

archive = namespace.model('Archive', {
    'Algorithm': fields.String(
        required=True,
        description="Machine Learning Algorithm"
    ),
    'Year': fields.String(
        required=True,
        description="Year of the classification"
    ),
})

def extract(ras_ds):
    geot = ras_ds.GetGeoTransform()
    width = ras_ds.RasterXSize
    height = ras_ds.RasterYSize

    minx = geot[0]  # lower left x
    miny = geot[3] + width * geot[4] + height * geot[5]  # lower left y
    maxx = geot[0] + width * geot[1] + height * geot[2]  # upper right x
    maxy = geot[3]  # upper right y

    # get CRS from dataset
    crs = osr.SpatialReference()
    crs.ImportFromWkt(ras_ds.GetProjectionRef())
    # create lat/long crs with WGS84 datum
    crsGeo = osr.SpatialReference()
    crsGeo.ImportFromEPSG(4326)  # 4326 is the EPSG id of lat/long crs
    t = osr.CoordinateTransformation(crs, crsGeo)
    latlong = []
    point1 = t.TransformPoint(minx, miny)
    point2 = t.TransformPoint(maxx, maxy)
    latlong.append(point1[1])
    latlong.append(point1[0])
    latlong.append(point2[1])
    latlong.append(point2[0])
    return latlong

@namespace.route('')
class Archive(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.response(201, 'Created')
    @namespace.expect(archive)
    def post(self):
        '''Post method for segmentation of an given lat/long bounding box'''
        data = request.json
        year = data['Year']
        algorithm = data['Algorithm']
        return {'message': "Created!"}, 201

    def get(self):
        data = request.json
        year = data['Year']
        algorithm = data['Algorithm']
        try:
           filename = 'utilis/tmp/archived/'+year+'/'+algorithm+year+'.tif'
           #latlong=extract(filename)
           img=Image.open(filename)
           img.save("utilis/tmp/archive.png")

        except FileNotFoundError:
            print("Wrong file or file path")
        return send_file("utilis/tmp/archive.png", as_attachment=True, attachment_filename="archive.png", mimetype='image/jpeg')