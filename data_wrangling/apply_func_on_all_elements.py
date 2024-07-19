import pandas as pd

# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

# load the data 
dataframe = pd.read_csv(url)

# create the function that will be applied 
def uppercase(x):
    return x.upper()

upper_name = dataframe['Name'].apply(uppercase)[0:2]
print(upper_name)