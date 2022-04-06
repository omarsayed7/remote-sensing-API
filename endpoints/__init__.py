from flask import Blueprint
from flask_restplus import Api
from endpoints.segmentation import namespace as segmentation_ns
from endpoints.upload import namespace as upload_file
from endpoints.segmentation_upload import namespace as seg_upload
from endpoints.archive import namespace as archive
from endpoints.sign_in import namespace as sign_in
from endpoints.sign_up import namespace as sign_up
from endpoints.contact_us import namespace as contact_us

blueprint = Blueprint('api', __name__, url_prefix='/api')
api_extension = Api(blueprint, title='Remote Sensing AI',
                    version='1.0',
                    description='Remote Sensing AI web API using Python Flask',
                    doc='/Swagger')

api_extension.add_namespace(segmentation_ns)
api_extension.add_namespace(upload_file)
api_extension.add_namespace(seg_upload)
api_extension.add_namespace(archive)
api_extension.add_namespace(sign_in)
api_extension.add_namespace(sign_up)
api_extension.add_namespace(contact_us)

