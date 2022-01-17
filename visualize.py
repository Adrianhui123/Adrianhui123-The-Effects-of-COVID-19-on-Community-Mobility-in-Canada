"""
CSC110 Final Project: The Effects of Covid-19 on Movement Trends in Canada, visuals file

This file does all the visualization of the data such as scatterplots
and bar graphs.
"""
import pandas
import matplotlib.pyplot as plt
import python_ta

from province_class import Province
from process_data import categories_extended, provinces


def histogram(df: pandas.DataFrame, title: str) -> None:
    """
    Creates a histogram based on given dataframe.
    """
    plt.figure('Histogram')
    df.plot(kind='hist', color='blue', edgecolor='black', figsize=(10, 7))
    plt.title('Distribution of ' + title + ' percent change from baseline for all provinces/territories', size=18)
    plt.xlabel(title, size=14)
    plt.ylabel('Frequency', size=14)


def find_elbow(dist: list[float]) -> int:
    """
    Prompts user to choose number of clusters for k-means clustering
    based on the inertia of 1 - 8 clusters and returns an int representing
    the number of clusters.
    """
    print('')
    print('Inertia for k clusters: ')

    for i in range(len(dist)):
        print(str(i + 1) + ' clusters: ' + str(dist[i]))

    while True:
        user = int(input('How many clusters do you want (Between 1 and 8 inclusive): '))
        if 1 <= user <= 8:
            return user


def calculate_z_score(province: Province, category_key: str, mobility_percent: int) -> float:
    """
    Return the z-score that compares a mobility percentage to a province's percent average for the specified
    mobility category.

    Preconditions:
        - all(mobility_percentage in df.loc[:, category_key])
    """
    standard_deviation = province.data[category_key].std(axis=0)
    mean = province.data[category_key].mean(axis=0)
    z_score = (mobility_percent - mean) / standard_deviation

    return z_score


def bar_graph(provinces_territories: list[Province], mobility_category: str) -> None:
    """
    Creates a bar graph comparing percent average of provinces and territories in the
    specified mobility category.
    """
    averages = []  # y-axis
    # get str of each province/territory to create labels
    labels = [name for name in provinces if provinces[name] in provinces_territories]

    # iterating through list of provinces/territories to obtain the average percent
    for province in provinces_territories:
        averages.append(province.data[mobility_category].mean(axis=0))

    plt.figure('Average Percent Change per Province for ' + ' '.join(str.split(mobility_category, '_')), figsize=(9, 5))
    plt.title('Average Percent Change per Province for ' + ' '.join(str.split(mobility_category, '_')))
    plt.xlabel('Provinces')
    plt.ylabel('Average Percent')
    plt.bar(labels, averages)


def bar_graph_two(province_territory: Province) -> None:
    """
    Creates a bar graph comparing all average percentages of each mobility category
    of the province.
    """
    averages = []  # y-axis
    labels = []  # x-axis

    # iterating through the dictionary so I can obtain the average percent for each category
    for category in categories_extended:
        labels.append(category)
        averages.append(province_territory.data[categories_extended[category]].mean(axis=0))

    plt.figure('Average Percent Change per Mobility Category of ' + province_territory.province_name, figsize=(9, 5))
    plt.title('Average Percent Change per Mobility Category of ' + province_territory.province_name)
    plt.xlabel('Mobility Category')
    plt.ylabel('Average Percent')
    plt.bar(labels, averages)


def data_picker(p_choice: str, name: str) -> pandas.DataFrame:
    """
    Returns a specific piece of data based on the given province and category.
    """
    if name == 'Transit':
        return provinces[p_choice].transit_stations_percent
    elif name == 'Work':
        return provinces[p_choice].work_places_percent
    elif name == 'Retail and Recreation':
        return provinces[p_choice].retail_and_recreation_percent
    elif name == 'Residential':
        return provinces[p_choice].residential_percent
    elif name == 'Parks':
        return provinces[p_choice].parks_percent
    elif name == 'Grocery':
        return provinces[p_choice].grocery_and_pharmacy_percent
    else:
        return provinces[p_choice].transit_stations_percent


if __name__ == '__main__':
    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'matplotlib', 'numpy', 'pandas', 'scikit_learn', 'datetime'],
        'allowed-io': ['histogram', 'find_elbow', 'bar_graph', 'bar_graph_two'],
        'max-line-length': 120,
        'disable': ['R1705', 'C0200']
    })

    import doctest

    doctest.testmod()
