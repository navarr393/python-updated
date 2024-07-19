# in this file we take a look at how to delete a column
import pandas as pd

# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

# Load data
dataframe = pd.read_csv(url)

# Delete column
dataframe.drop('Age', axis=1).head(2)

# Drop columns
dataframe.drop(['Age', 'Sex'], axis=1).head(2)
print(dataframe.head(5))