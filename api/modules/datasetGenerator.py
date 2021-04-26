import json
import pandas as pd
from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.sql.functions import col, column, round as roundp

class datasetGenerator(object):
    """
    Class responsible for parse a config.json file into a avaiable dataset.
    Data treatment using pandas.
    """
    def __init__(self, json_path='config.json'):
        
        self._json_path = json_path
        self._data_filename = self._get_filename_from_json()
        self._dataframe = self._create_dataframe()

    def _get_filename_from_json(self):

        with open(self._json_path) as config_file:

            config_info = json.load(config_file)

        return config_info['filename']

    def _create_dataframe(self):
        
        complete_filename = ''.join(['src/', self._data_filename])
        dataframe = pd.read_csv(complete_filename)
        return dataframe

    @property
    def dataframe(self):

        return self._dataframe

class datasetGeneratorSpark(datasetGenerator):

    def _create_dataframe(self):
        
        complete_filename = ''.join(['src/', self._data_filename])
        sc = SparkContext()
        sqlContext = SQLContext(sc)
        dataframe = sqlContext.read.option("header", True).csv(complete_filename)
        dataframe = dataframe.withColumn("car_value", col("car_value").cast("double"))
        return dataframe