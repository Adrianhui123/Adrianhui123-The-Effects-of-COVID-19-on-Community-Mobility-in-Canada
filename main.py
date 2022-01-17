"""
CSC110 Final Project: The Effects of Covid-19 on Movement Trends in Canada, main file

This file prompts the user for the data needed to run all the
calculations and visualize the changes of mobility throughout
Canada.
"""
from m_learning import lin_reg, k_means
from visualize import data_picker, categories_extended, \
    histogram, bar_graph, bar_graph_two, calculate_z_score
from process_data import provinces, canada, provinces_list

print('Provinces and Territories: \n BC \n AB \n SK \n '
      'MB \n ON \n QC \n NL \n NB \n PE \n NS \n YT \n NT \n NU')
user_plot_choice = input('Choose a Province: ')
user_plot_choice2 = input('Choose another province to compare with your first choice: ')

print('')

print('Categories of Mobility: \n Transit \n Work \n'
      ' Retail and Recreation \n Grocery \n Parks \n Residential')
user_data_choice1 = input('Choose a category of mobility to plot over time: ')
user_data_choice2 = input('Choose another category of mobility to compare its correlation to your first choice: ')
hist_choice = input('Choose another category of mobility to see its distribution throughout Canada: ')

plot_x, plot_y = data_picker(user_plot_choice, user_data_choice1),\
                 data_picker(user_plot_choice, user_data_choice2)

provinces[user_plot_choice].plot_data(plot_x, user_data_choice1)

print('')

lin_reg(plot_x, plot_y, user_data_choice1, user_data_choice2)
k_means(provinces[user_plot_choice].data, provinces[user_plot_choice2].data, categories_extended[user_data_choice1],
        categories_extended[user_data_choice2])
histogram(canada.data[categories_extended[hist_choice]], hist_choice)

bar_graph(provinces_list, categories_extended[user_data_choice1])
bar_graph_two(provinces[user_plot_choice])

print('')
print('Standard deviation of ' + hist_choice + ' mobility throughout Canada: '
      + str(canada.data[categories_extended[hist_choice]].std(axis=0)))
val = input('Find Z-score of: ')
print(str(calculate_z_score(canada, categories_extended[hist_choice], int(val))))
