"""
CSC110 Final Project: The Effects of Covid-19 on Movement Trends in Canada, data processing file

This file processes all the raw data from the CSV file and
organizes it into usable dataframes and Province classes
"""
import pandas as pd
import python_ta

from province_class import Province

# get CSV file and make the DataFrame
df = pd.read_csv("2020_CA_Region_Mobility_Report_Edited_2.csv")
print(df.head())

# provinces and territories
canada = Province(df.iloc[2:322])

AB = Province(df.iloc[323:643])  # Alberta
BC = Province(df.iloc[644:964])  # British Columbia
MB = Province(df.iloc[965:1259])  # Manitoba
NB = Province(df.iloc[1260:1520])  # New Brunswick
NL = Province(df.iloc[1521:1765])  # Newfoundland and Labrador
NS = Province(df.iloc[1766:2043])  # Nova Scotia
ON = Province(df.iloc[2044:2364])  # Ontario
QC = Province(df.iloc[2365:2685])  # Quebec
SK = Province(df.iloc[2686:2975])  # Saskatchewan

PE = Province(df.iloc[2976:3187])  # Prince Edward County, not the actual province
NW = Province(df.iloc[3188:3483])  # Northwest Territories
YT = Province(df.iloc[3484:3758])  # Yukon Territories
NU = Province(df.iloc[3759:4005])  # Nunavut

provinces = {'BC': BC, 'AB': AB, 'MB': MB, 'NB': NB, 'NL': NL, 'NS': NS, 'ON': ON, 'QC': QC,
             'SK': SK, 'PE': PE, 'NW': NW, 'YT': YT, 'NU': NU}

provinces_list = [BC, AB, MB, NB, NL, NS, ON, QC, SK, PE, NW, YT, NU]

categories = {'Transit', 'Work', 'Retail and Recreation', 'Grocery', 'Parks', 'Residential'}
categories_extended = {'Transit': 'transit_stations_percent_change_from_baseline',
                       'Work': 'workplaces_percent_change_from_baseline',
                       'Retail and Recreation': 'retail_and_recreation_percent_change_from_baseline',
                       'Grocery': 'grocery_and_pharmacy_percent_change_from_baseline',
                       'Parks': 'parks_percent_change_from_baseline',
                       'Residential': 'residential_percent_change_from_baseline'}

if __name__ == '__main__':
    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'matplotlib', 'numpy', 'pandas', 'scikit_learn', 'datetime'],
        'max-line-length': 120,
        'disable': ['R1705', 'C0200']
    })

    import doctest

    doctest.testmod()
