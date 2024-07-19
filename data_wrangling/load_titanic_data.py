# in this file we load data about titanic

import pandas as pd

# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

# load data as a dataframe
dataframe = pd.read_csv(url)

#show the first 5 rows
print(dataframe.head(5))