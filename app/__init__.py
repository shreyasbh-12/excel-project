import os
from flask import Flask
# from flask_cors import CORS
from flask_restful import Api
# from flask_sqlalchemy import SQLAlchemy
from app.config import Config



app = Flask(__name__)
api = Api(app)
# CORS(app)

app.config.from_object(Config)

# output folder 
output_folder = app.config['OUTPUT_FOLDER']

app.config['OUTPUT_FOLDER'] = os.path.join(os.getcwd(), output_folder)


# from app import routes, utils
from app import operations

# Register the endpoint
api.add_resource(operations.TransformData, '/dashboard')