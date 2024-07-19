import pandas as pd

# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

# load the data into dataframe
dataframe = pd.read_csv(url)

# print the first 2 names uppercased 
for name in dataframe['Name'][0:2]:
    print(name.upper())

# show the first 2 names uppercased using list comperhension
upper_name = [name.upper() for name in dataframe['Name'][0:2]]
print(upper_name)