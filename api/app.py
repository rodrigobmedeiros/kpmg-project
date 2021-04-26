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

    # Data treatment using pandas
    data_info = datasetGenerator('config.json')

    grouped_data = dataGrouper(data_info.dataframe)

    # Data treatment using spark
    data_info_spark = datasetGeneratorSpark('config.json')

    grouped_data_by_city = dataGrouperSpark(data_info_spark.dataframe)

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

    @app.route('/mean-values-per-cities', methods=['GET'])
    def get_mean_values_per_cities():

        return jsonify({'sucess': True,
                        'manufacturer_mean_values': grouped_data_by_city.formatted_data})

    @app.route('/mean-values-per-cities/<city>', methods=['GET'])
    def get_mean_value_by_manufacturer(city):

        # default column name created when mean was applied.
        avg_column = 'avg(car_value)'
        filtered_city = grouped_data_by_city.data_agg_by_mean_value['city' == city]
        city_mean_value = filtered_city[avg_column]      

        return jsonify({'sucess': True,
                        'manufacturer': city,
                        'mean_value': round(city_mean_value, 2)})

    return app