import pandas as pd

class dataGrouper(object):

    def __init__(self, dataframe: pd.DataFrame):

        self._dataframe = dataframe 
        self._data_grouped_by_manufacturer = self._group_by_manufacturer()
        self._data_agg_by_mean_value = self._agg_by_mean()
        self._formatted_data = self._format_data()

    def _group_by_manufacturer(self):

        return self.dataframe.groupby('car_make')

    def _agg_by_mean(self):

        return self._data_grouped_by_manufacturer.agg('mean')[['car_value']]

    def _format_data(self):

        formatted_data = []

        for row in self._data_agg_by_mean_value.iterrows():
            
            car_make = row[0]
            mean_car_value = round(row[1][0], 2)
            formatted_data.append({'car_make': car_make, 'mean_car_value': mean_car_value})

        return formatted_data

    @property
    def data_agg_by_mean_value(self):

        return self._data_agg_by_mean_value

    @property
    def formatted_data(self):

        return self._formatted_data