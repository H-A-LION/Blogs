#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

# Example data for GDP per capita, life expectancy, and population
gdp_cap = [950, 2000, 3000, 15000, 35000, 47000, 60000, 75000, 91000, 120000]
life_exp = [49, 55, 66, 70, 75, 76, 78, 79, 81, 82]
pop = [10, 12, 15, 25, 35, 45, 55, 65, 75, 85]  # Population in millions

# Define the dictionary mapping continents to colors
continent_colors = {
    'Asia': 'red',
    'Europe': 'green',
    'Africa': 'blue',
    'Americas': 'yellow',
    'Oceania': 'black'
}

#continents list
continents = ['Asia', 'Europe', 'Africa', 'Americas', 'Oceania', 'Asia', 'Europe', 'Africa', 'Americas', 'Oceania']

# Map the continents to colors
col = [continent_colors[continent] for continent in continents]

# Convert population to numpy array for size adjustment in scatter plot
np_pop = np.array(pop) * 2

# Create scatter plot
plt.scatter(gdp_cap, life_exp, s=np_pop, c=col, alpha= 0.8)

# Customize the plot with logarithmic scale and labels
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])

plt.savefig('xtick.png')
