# in this file we learn how to merge 2 dataframes the following is some info regarding merge:
# Inner
# Return only the rows that match in both DataFrames (e.g., return any row with an employee_id value appearing in both dataframe_employees and dataframe_sales).

# Outer
# Return all rows in both DataFrames. If a row exists in one DataFrame but not in the other DataFrame, fill NaN values for the missing values (e.g., return all rows in both dataframe_employee and dataframe_sales).

# Left
# Return all rows from the left DataFrame but only rows from the right DataFrame that match with the left DataFrame. Fill NaN values for the missing values (e.g., return all rows from dataframe_employees but only rows from dataframe_sales that have a value for employee_id that appears in dataframe_employees).

# Right
# Return all rows from the right DataFrame but only rows from the left DataFrame that match with the right DataFrame. Fill NaN values for the missing values (e.g., return all rows from dataframe_sales but only rows from dataframe_employees that have a value for employee_id that appears in dataframe_sales).


import pandas as pd

# To inner join, use merge with the on parameter to specify the column to merge on:
# Create DataFrame
employee_data = {'employee_id': ['1', '2', '3', '4'],
                 'name': ['Amy Jones', 'Allen Keys', 'Alice Bees',
                 'Tim Horton']}
dataframe_employees = pd.DataFrame(employee_data, columns = ['employee_id',
                                                              'name'])

# Create DataFrame
sales_data = {'employee_id': ['3', '4', '5', '6'],
              'total_sales': [23456, 2512, 2345, 1455]}
dataframe_sales = pd.DataFrame(sales_data, columns = ['employee_id',
                                                      'total_sales'])

# merge the 2 dataframes 
merged = pd.merge(dataframe_employees, dataframe_sales, on='employee_id')
print(merged)

# Merge DataFrames, specify outer join to display all info even if it is not there for a certain data.
merged = pd.merge(dataframe_employees, dataframe_sales, on='employee_id', how='outer')
print(merged)

# Merge DataFrames
merged = pd.merge(dataframe_employees, dataframe_sales, on='employee_id', how='left')
print(merged)

# merge the 2 dataframes and put employee_id on left, and 
merged = pd.merge(dataframe_employees,
         dataframe_sales,
         left_on='employee_id',
         right_on='employee_id')
print(merged)