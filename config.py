# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@127.0.0.1:5432/mydb'
DATABASE_CONNECT_OPTIONS = {}
