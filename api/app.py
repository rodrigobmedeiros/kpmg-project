import sys, os
from flask import Flask
from modules.datasetGenerator import datasetGenerator

def create_app(test_config=None):
    """
    Function used to define all end points and error handling.
    """
    app = Flask(__name__)
    data_info = datasetGenerator('config.json')
    print(data_info.dataframe.columns)

