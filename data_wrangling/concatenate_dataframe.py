# in this file we take a look at how to concatenate dataframes 
import pandas as pd

# Create DataFrame
data_a = {'id': ['1', '2', '3'],
          'first': ['Alex', 'Amy', 'Allen'],
          'last': ['Anderson', 'Ackerman', 'Ali']}
dataframe_a = pd.DataFrame(data_a, columns = ['id', 'first', 'last'])

# Create DataFrame
data_b = {'id': ['4', '5', '6'],
          'first': ['Billy', 'Brian', 'Bran'],
          'last': ['Bonder', 'Black', 'Balwner']}
dataframe_b = pd.DataFrame(data_b, columns = ['id', 'first', 'last'])

# Concatenate DataFrames by rows
row_combined = pd.concat([dataframe_a, dataframe_b], axis=0)
print(row_combined)

# we can use axis=1 to combine using columns
column_combine = pd.concat([dataframe_a, dataframe_b], axis=1)
print(column_combine)