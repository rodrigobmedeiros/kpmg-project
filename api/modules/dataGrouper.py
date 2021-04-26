import pandas as pd
from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.sql.functions import col, column, round as roundp

class dataGrouper(object):
    """
    Class responsible for grouping data considering manufacturers.
    """
    def __init__(self, dataframe):
        """
        Method responsible for initialize objects during its creation.

        args
        ----
        dataframe (pd.DataFrame) -> dataframe to br grouped.
        """
        self._dataframe = dataframe 
        self._data_grouped_by_manufacturer = self._group_by_manufacturer()
        self._data_agg_by_mean_value = self._agg_by_mean()
        self._formatted_data = self._format_data()

    def _group_by_manufacturer(self):
        """
        Method responsible to group data considering manunfacturer.

        return
        ------   
        data grouped by manufacturer.
        """
        return self._dataframe.groupby('car_make')

    def _agg_by_mean(self):
        """
        Method responsible for apply mean in car_value column in the grouped dataframe.

        return
        ------ 
        data aggregated by mean applied on car_value column.
        """
        return self._data_grouped_by_manufacturer.agg('mean')[['car_value']]

    def _format_data(self):
        """
        Method responsible for format data in a beautiful way to be retorned as a json object.

        return
        ------ 
        list of each manufacturer mean car value organized as dicts.
        """
        formatted_data = []

        for row in self._data_agg_by_mean_value.iterrows():
            
            car_make = row[0]
            mean_car_value = round(row[1][0], 2)
            formatted_data.append({'car_make': car_make, 'mean_car_value': mean_car_value})

        return formatted_data

    @property
    def data_agg_by_mean_value(self):
        """
        Method responsible for access data aggregated by mean.

        return
        ------
        Expose data agg by mean for external use.
        """
        return self._data_agg_by_mean_value

    @property
    def formatted_data(self):
        """
        Method responsible for formatted data.

        return
        ------
        Expose formatted data for external use.
        """
        return self._formatted_data

class dataGrouperSpark(dataGrouper):
    """
    Class based on dataGrouper class used to treat spark dataframe instead of pandas dataframe.
    """
    def _group_by_manufacturer(self):
        
        return self._dataframe.groupby('city')

    def _agg_by_mean(self):
        df_grouped = self._data_grouped_by_manufacturer.mean('car_value')
        df_grouped = df_grouped.withColumn("avg(car_value)", roundp(col("avg(car_value)"), 2))
        df_grouped = df_grouped.rdd.collect()
        return df_grouped

    def _format_data(self):

        formatted_data = []

        for row in self._data_agg_by_mean_value:
    
            formatted_data.append({'car_make': row['city'],
                                   'mean_car_value': row['avg(car_value)']})

        return formatted_data