# in this file we take a look at how to use boolean conditons to view data
import pandas as pd

# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

# Load data
dataframe = pd.read_csv(url)

# Delete rows, show first three rows of output, excludes 'male'
print(dataframe[dataframe['Sex'] != 'male'].head(3))

# Delete row, show first two rows of output
dataframe[dataframe['Name'] != 'Allison, Miss Helen Loraine'].head(2)

# Delete first row using index, show first two rows of output
dataframe[dataframe.index != 0].head(2)