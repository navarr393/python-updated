# in this file we take a look at how to slice a dataframe and select an interval
import pandas as pd

# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

dataframe = pd.read_csv(url)

# select the first row
print(dataframe.iloc[0])

# select the 2nd, third and fourth rows
print(dataframe.iloc[1:4])

# select all rows up to and including 4th row
print(dataframe.iloc[:4])

# Set index to name
dataframe = dataframe.set_index(dataframe['Name'])

# Show row
dataframe.loc['Allen, Miss Elisabeth Walton']