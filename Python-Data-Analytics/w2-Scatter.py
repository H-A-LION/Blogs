#!/usr/bin/env python3
import matplotlib.pyplot as plt

gdp_cap=[1000,2000,3000,4000,5000]
life_exp=[50,60,70,65,80]

#Basic scatter plot, log scale
plt.scatter(gdp_cap,life_exp)
plt.xscale('log')

#strings for label and title
xlab='GDP per Capital'
ylab='Life expectation [in years]'
title='World Development in 2007'

#add axis label
plt.xlabel(xlab)
plt.ylabel(ylab)

#add title
plt.title(title)

plt.savefig('scatter.png')
