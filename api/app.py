import sys, os
from flask import Flask, jsonify
from modules.datasetGenerator import datasetGenerator
from modules.dataGrouper import dataGrouper

def create_app(test_config=None):
    """
    Function used to define all end points and error handling.
    """
    app = Flask(__name__)
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

    data_info = datasetGenerator('config.json')

    grouped_data = dataGrouper(data_info.dataframe)

    @app.route('/mean-values-per-manufacturer', methods=['GET'])
    def get_mean_values_per_manufacturer():

        return jsonify({'sucess': True,
                        'manufacturer_mean_values': grouped_data.formatted_data})


    @app.route('/mean-values-per-manufacturer/<manufacturer>', methods=['GET'])
    def get_mean_value_by_manufacturer(manufacturer):

        manufacturer_mean_value = grouped_data.data_agg_by_mean_value.loc[manufacturer].values[0]        

        return jsonify({'sucess': True,
                        'manufacturer': manufacturer,
                        'mean_value': round(manufacturer_mean_value, 2)})



    return app