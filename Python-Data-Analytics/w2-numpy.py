#!/usr/bin/env python3
import numpy as np

#Create 2D NumPy array
data_2d=np.array([
    [1.73,65.4],
    [1.68,59.2],
    [1.71,63.6],
    [1.89,88.9],
    [1.79,68.7]
])

#Calculate standard deviation of the first column
std_dev_2d_col1=np.std(data_2d[:,0])
print('standard deviaton of first column',std_dev_2d_col1)

#Calculate mean of the first column
mean_2d_col1=np.mean(data_2d[:,0])
print('mean of first column',mean_2d_col1)

#Calculate median of the first column
median_2d_col1=np.median(data_2d[:,0])
print('Median of first column',median_2d_col1)

#Calculate standard deviation of the Second column
std_dev_2d_col2=np.std(data_2d[:,1])
print('standard deviation of second column',std_dev_2d_col2)

# Calculate correlation between the two columns
correlation = np.corrcoef(data_2d[:, 0], data_2d[:, 1])[0, 1]
print("Correlation between columns:", correlation)

