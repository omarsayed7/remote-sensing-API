from http.client import HTTPResponse
from socket import socket
from flask import request, Response, send_file, jsonify, make_response
from flask_restplus import Namespace, Resource, fields
from http import HTTPStatus
from numpy import require
from PIL import Image
from application.utilis.inference import inference, fake_img_resp
from application.utilis.mapbox_request import mapbox_request
try:
    import osr
    import gdal
except ImportError:
    from osgeo import osr, gdal

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
        filename = 'application/utilis/tmp/archived/'+year+'/'+algorithm+year+'.tif'
        open('application/utilis/tmp/archive.txt', 'w').close()
        archive_file = open("application/utilis/tmp/archive.txt", "a")
        archive_file.write(filename)
        archive_file.close()
        col_matrix = open('application/utilis/tmp/archived/'+year+'/' +
                          algorithm+year+'.txt').readlines()
        latlong = extract(gdal.Open(filename))
        resp = resp = jsonify({'message': "Created!"}, {'col_matrix': col_matrix}, {
            'bbox': "[["+str(latlong[0])+","+str(latlong[1])+"],["+str(latlong[2])+","+str(latlong[3])+"]]"})
        resp.status_code = 201
        return resp

    def get(self):
        # data = request.json
        # print(request,"45645135")
        # year = data['Year']
        # algorithm = data['Algorithm']

        try:
            filename = open('application/utilis/tmp/archive.txt').readlines()
            print(filename, "189456154")
        #    filename = 'utilis/tmp/archived/'+year+'/'+algorithm+year+'.tif'
            img = Image.open(filename[0])
            img.save("application/utilis/tmp/archive.png")
        except FileNotFoundError:
            print("Wrong file or file path")
        return send_file("application/utilis/tmp/archive.png", as_attachment=True, attachment_filename="archive.png", mimetype='image/jpeg')
