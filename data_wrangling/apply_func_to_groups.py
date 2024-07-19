# in this file we learn how to group by Column in this case 'Sex'
import pandas as pd

# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

# load data 
dataframe = pd.read_csv(url)

# group rows and apply function to rows
group = dataframe.groupby('Sex').apply(lambda x : x.count())
print(group)