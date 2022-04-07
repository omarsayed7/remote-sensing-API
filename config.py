# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'postgresql://hexykuftyxhmza:137066fd386156ba6ea41c4af44e4319e079877b59a6b1f8586fe486b9396cb6@ec2-52-48-159-67.eu-west-1.compute.amazonaws.com:5432/d3c3mlb83bbmcq'
SQLALCHEMY_TRACK_MODIFICATIONS = False
