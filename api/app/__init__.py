import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
from flask import Flask
from api.modules.datasetGenerator import datasetGenerator

def create_app(test_config=None):
    """
    Function used to define all end points and error handling.
    """
    app = Flask(__name__)
    df = datasetGenerator()
    print(df.columns)


print(os.path.dirname(os.path.realpath(__file__)))

    
