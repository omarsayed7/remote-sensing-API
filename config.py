# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'postgres://nfjascluiygyic:e848835da75e1cf517713aecbc0007f1f4764adc27940fd2b1942d138dcf4145@ec2-99-81-137-11.eu-west-1.compute.amazonaws.com:5432/d7cdtdp01s763u'
SQLALCHEMY_TRACK_MODIFICATIONS = False
