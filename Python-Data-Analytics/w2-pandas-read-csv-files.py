#Reading csv file with pandas
import pandas as pd

housing = pd.read_csv('path-to/file.csv')



#Selecting and accessing Data

#Method 1 : Square brackets


housing[['longitude']]




#Method 2 : Loc and iloc

housing.loc[: , ['longitude', 'latitude']]


#iloc

#housing.iloc[[1] , [0, 4]]
