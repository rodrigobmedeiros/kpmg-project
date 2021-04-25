import os
import json
import pandas as pd

class datasetGenerator(object):
    """
    Class responsible for parse a config.json file into a avaiable dataset.
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

datasetGenerator()