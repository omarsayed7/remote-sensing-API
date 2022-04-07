# Run a test server.
from flask_cors import CORS
from application import app

CORS(app)

if __name__ == "__main__":
    app.run()
