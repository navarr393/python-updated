# in this file we take a look at how to find unique values
import pandas as pd

# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

# load the data 
dataframe = pd.read_csv(url)

# select unique values 
print(dataframe['Sex'].unique())

# prints the number that unique value appears
print(dataframe['Sex'].value_counts())

print(dataframe['PClass'].value_counts())

# show the number of unique values in PClass, returns 4
print(dataframe['PClass'].nunique())