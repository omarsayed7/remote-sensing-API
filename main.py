from flask import Flask, request
from endpoints import blueprint as segmentation_endpoint

app = Flask(__name__)
app.register_blueprint(segmentation_endpoint)

if __name__ == '__main__':
    app.run(debug=True)
