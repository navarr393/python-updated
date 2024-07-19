# in this file we take a look at how to handle missing files.
import pandas as pd
import numpy as np

# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

# load the data 
dataframe = pd.read_csv(url)

# Select missing values, show two rows
print(dataframe[dataframe['Age'].isnull()].head(2))

# replace NaN values with numpy
dataframe['Sex'] = dataframe['Sex'].replace('male', np.nan)

# Get a single null row
null_entry = dataframe[dataframe["Age"].isna()].head(1)
print(null_entry)

# Fill all null values with the mean age of passengers
null_entry.fillna(dataframe["Age"].mean())