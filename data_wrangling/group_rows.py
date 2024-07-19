# Load library
import pandas as pd

# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

# Load data
dataframe = pd.read_csv(url)

# Group rows by the values of the column 'Sex', calculate mean # of each group
print(dataframe.groupby('Sex').mean(numeric_only=True))

# Group rows, count rows
print(dataframe.groupby('Survived')['Name'].count())

# Group rows, calculate mean
print(dataframe.groupby(['Sex','Survived'])['Age'].mean())