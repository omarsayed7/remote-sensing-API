from flask import Blueprint
from flask_restplus import Api
from application.endpoints.segmentation import namespace as segmentation_ns
from application.endpoints.upload import namespace as upload_file
from application.endpoints.segmentation_upload import namespace as seg_upload
from application.endpoints.archive import namespace as archive
blueprint = Blueprint('api', __name__, url_prefix='/api')
api_extension = Api(blueprint, title='Remote Sensing AI',
                    version='1.0',
                    description='Remote Sensing AI web API using Python Flask',
                    doc='/Swagger')

api_extension.add_namespace(segmentation_ns)
api_extension.add_namespace(upload_file)
api_extension.add_namespace(seg_upload)
api_extension.add_namespace(archive)
