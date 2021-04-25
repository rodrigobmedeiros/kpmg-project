import sys, os
from flask import Flask, jsonify
from modules.datasetGenerator import datasetGenerator
from modules.dataGrouper import dataGrouper

def create_app(test_config=None):
    """
    Function used to define all end points and error handling.
    """
    app = Flask(__name__)

    data_info = datasetGenerator('config.json')

    grouped_data = dataGrouper(data_info.dataframe)

    @app.route('/mean-values-per-manufacturer', methods=['GET'])
    def get_mean_values_per_manufacturer():

        return jsonify({'sucess': True, 'manufacturer_mean_values': grouped_data.formatted_data})

    return app