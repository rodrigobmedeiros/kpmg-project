import sys, os
from flask import Flask, jsonify
from modules.datasetGenerator import datasetGenerator, datasetGeneratorSpark
from modules.dataGrouper import dataGrouper, dataGrouperSpark

def create_app():
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
        """
        Function responsible for return mean car values by manufacturer.

        return
        ------
        json with all mean car values by manufacturer included.
        """
        return jsonify({'success': True,
                        'manufacturer_mean_values': grouped_data.formatted_data})


    @app.route('/mean-values-per-manufacturer/<manufacturer>', methods=['GET'])
    def get_mean_value_by_manufacturer(manufacturer):
        """
        Function responsible for return mean car values by specific manufacturer.

        args
        ----
        manufacturer -> specific manufacturing included in the endpoint.

        return
        ------                 
        json with mean car value by specific manufacturer.
        """
        manufacturer_mean_value = grouped_data.data_agg_by_mean_value.loc[manufacturer].values[0]        

        return jsonify({'success': True,
                        'manufacturer': manufacturer,
                        'mean_value': round(manufacturer_mean_value, 2)})

    @app.route('/mean-values-per-city', methods=['GET'])
    def get_mean_values_per_city():
        """
        Function responsible for return mean car values by city.

        return
        ------
        json with all mean car values by city included.
        """
        return jsonify({'sucess': True,
                        'city_mean_values': grouped_data_by_city.formatted_data})

    @app.route('/mean-values-per-city/<city>', methods=['GET'])
    def get_mean_value_per_city(city):
        """
        Function responsible for return mean car values by specific city.

        args
        ----
        manufacturer -> specific city included in the endpoint.

        return
        ------                 
        json with mean car value by specific city.
        """

        # default column name created when mean was applied.
        avg_column = 'avg(car_value)'
        filtered_city = grouped_data_by_city.data_agg_by_mean_value['city' == city]
        city_mean_value = filtered_city[avg_column]      

        return jsonify({'success': True,
                        'city': city,
                        'mean_value': city_mean_value})
    
    return app