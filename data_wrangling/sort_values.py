# in this file we take a look at how to sort data by values we provide
import pandas as pd

# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

# load the data 
dataframe = pd.read_csv(url)

# sort the dataframe by age and show 2 rows
print(dataframe.sort_values(by=["Age"]).head(2))