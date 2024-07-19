# in this file we learn how to create a new dataframe

import pandas as pd

# create a dictionary
dictionary = {
    "Name": ['Jacky Jackson', 'Steven Stevenson'],
    "Age": [38, 25],
    "Driver": [True, False]
}

# create a dataframe from the dictionary
dataframe = pd.DataFrame(dictionary)

# print the dataframe
print(dataframe)

# add new columns to the dataframe using a list of values
dataframe["Eyes"] = ["Brown", "Green"]
print(dataframe)