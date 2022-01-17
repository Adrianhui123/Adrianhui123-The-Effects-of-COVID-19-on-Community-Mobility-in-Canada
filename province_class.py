"""
CSC110 Final Project: The Effects of Covid-19 on Movement Trends in Canada, province class file

This file creates the Province class which stores the
data from the CSV file into lists that are easy
to manipulate and perform calculations on.
"""
import datetime
import pandas
import matplotlib.pyplot as plt
import python_ta


class Province:
    """
    A class representing a province.

    Instance Attributes:
        - data: A dataframe consisting of data related to the province's mobility
        - dates: The list of days of the province
        - province_name: The name of the province
        - retail_and_recreation_percent: The percentage change of mobility in retail and recreational areas
        - grocery_and_pharmacy_percent: The percentage change of mobility in grocery
          and pharmaceutical areas
        - parks_percent: The percentage change of mobility in parks
        - transit_stations_percent: The percentage change of mobility in transit stations
        - work_places_percent: The percentage change of mobility in work places
        - residential_percent: The percentage change of mobility in residential areas

    Representation Invariants:
        - province_name != ''
        - dates != []
        - retail_and_recreation_percent != []
        - grocery_and_pharmacy_percent != []
        - parks_percent != []
        - transit_stations_percent != []
        - work_places_percent != []
        - residential_percent != []
    """
    data: pandas.DataFrame
    dates: list[datetime]
    province_name: str
    retail_and_recreation_percent: list[int]
    grocery_and_pharmacy_percent: list[int]
    parks_percent: list[int]
    transit_stations_percent: list[int]
    work_places_percent: list[int]
    residential_percent: list[int]

    def __init__(self, data: pandas.DataFrame) -> None:
        self.data = data
        dates = data['date'].values.reshape(-1, 1)

        self.province_name = data[['sub_region_1']].iloc[0, 0]
        self.dates = [datetime.date(int(x[0].split('-')[0]), int(x[0].split('-')[1]),
                                    int(x[0].split('-')[2])) for x in dates]
        self.retail_and_recreation_percent = data['retail_and_recreation_percent_change_from_baseline'].values.reshape(
            -1, 1)
        self.grocery_and_pharmacy_percent = data['grocery_and_pharmacy_percent_change_from_baseline'].values.reshape(-1,
                                                                                                                     1)
        self.parks_percent = data['parks_percent_change_from_baseline'].values.reshape(-1, 1)
        self.transit_stations_percent = data['transit_stations_percent_change_from_baseline'].values.reshape(-1, 1)
        self.work_places_percent = data['workplaces_percent_change_from_baseline'].values.reshape(-1, 1)
        self.residential_percent = data['residential_percent_change_from_baseline'].values.reshape(-1, 1)

    def average(self, mobility: list) -> float:
        """
        Returns the average percent change of mobility of a given mobility category.
        """
        return sum(mobility) / len(mobility)

    def plot_data(self, y: list[int], name: str) -> None:
        """
        Creates a scatter plot from the given data.
        """
        plt.figure(name + ' percent change from baseline over time')
        plt.scatter(self.dates, y, color='blue')
        plt.xlabel('Date', size=12)
        plt.ylabel('Percent Change', size=12)
        plt.show()


if __name__ == '__main__':
    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'matplotlib', 'numpy', 'pandas', 'scikit_learn', 'datetime'],
        'allowed-io': ['plot_data'],
        'max-line-length': 120,
        'disable': ['R1705', 'C0200']
    })

    import doctest

    doctest.testmod()
