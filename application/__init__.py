from flask import Flask, request
from application.endpoints import blueprint as segmentation_endpoint
from flask_ngrok import run_with_ngrok
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# Configurations
app.config.from_object('config')

db = SQLAlchemy(app)

# run_with_ngrok(app)
app.register_blueprint(segmentation_endpoint)

db.create_all()
