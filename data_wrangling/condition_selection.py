# in this file we learn how to select data based on a condition
import pandas as pd

# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

dataframe = pd.read_csv(url)

# show the first 2 rows where column is 'sex' and value is 'female'
print(dataframe[dataframe['Sex'] == 'female'].head(2))

# Filter rows
print(dataframe[(dataframe['Sex'] == 'female') & (dataframe['Age'] >= 65)])