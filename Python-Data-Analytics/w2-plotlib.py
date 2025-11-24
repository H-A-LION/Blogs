#!/usr/bin/env python3
import matplotlib.pyplot as plt

gdp_cap=[12345,23456,34567,45678,56789]
life_exp=[70,72,74,76,78]

#print the last item from both lists
print('The last item from gdp_cap is: ',gdp_cap[-1])
print('The last item from life_exp is: ',life_exp[-1])

#plotting the data
plt.plot(gdp_cap,life_exp)

#labeling the axis
plt.xlabel('GDP per Capita')
plt.ylabel('Life Expectancy')

#Save the plot to a file instead of showing 
plt.savefig('gdp_vs_life.png', dpi=300, bbox_inches='tight')
print("Plot saved as 'gdp_vs_life.png'")

#Display the plot
#plt.show()
