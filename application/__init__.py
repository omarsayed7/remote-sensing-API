from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nfjascluiygyic:e848835da75e1cf517713aecbc0007f1f4764adc27940fd2b1942d138dcf4145@ec2-99-81-137-11.eu-west-1.compute.amazonaws.com:5432/d7cdtdp01s763u'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'hi'

db = SQLAlchemy(app)

from application.endpoints import blueprint as segmentation_endpoint
app.register_blueprint(segmentation_endpoint)

db.create_all()
db.session.commit()
