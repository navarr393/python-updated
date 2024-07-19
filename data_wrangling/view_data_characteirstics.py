# in this file we learn how to view data characteristics
import pandas as pd

# view the first rows using head()
# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

# load data
dataframe = pd.read_csv(url)

# show the first 2 rows 
print(dataframe.head(2))

# take a look at the number of rows and columns in the form of (rows, columns)
print(dataframe.shape)

# We can get descriptive statistics for any numeric columns using describe:
print(dataframe.describe())

# if we need more info we can use the info method
print(dataframe.info())

# view the last few rows, 5 if we dont pass a number
print(dataframe.tail())