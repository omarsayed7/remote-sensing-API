from flask import Flask, request
from endpoints import blueprint as segmentation_endpoint
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)
app.register_blueprint(segmentation_endpoint)

if __name__ == '__main__':
    app.run()
