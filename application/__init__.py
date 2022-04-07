from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hexykuftyxhmza:137066fd386156ba6ea41c4af44e4319e079877b59a6b1f8586fe486b9396cb6@ec2-52-48-159-67.eu-west-1.compute.amazonaws.com:5432/d3c3mlb83bbmcq'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'hi'

db = SQLAlchemy(app)

from application.endpoints import blueprint as segmentation_endpoint
app.register_blueprint(segmentation_endpoint)

db.create_all()
db.session.commit()
