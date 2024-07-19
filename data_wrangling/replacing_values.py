# in this file we take a look at how to replace values of a dataframe
import pandas as pd

# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

# load the data 
dataframe = pd.read_csv(url)

# replace values and show 2 rows
# Replace "female" and "male" with "Woman" and "Man"
print(dataframe['Sex'].replace(["female", "male"], ["Woman", "Man"]).head(5))
# replace all values that contain 1 with One and show 2 rows
print(dataframe.replace(1, "One").head(2))

# using replace with regular expressions 
# replace 1st with First
print(dataframe.replace(r"1st", "First", regex=True).head(2))