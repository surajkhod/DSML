# 24. Perform the following operations using Python on a suitable data set,
# counting unique values of data, format of each column, converting variable
# data type (e.g. from long to short, vice versa), identifying missing values
# and filling in the missing values.


import pandas as pd

# Load the dataset (path is already given from previous context)
file_path = '/home/surajkhod/Coding/DSML/datasets/Covid Vaccine Statewise.csv'
data = pd.read_csv(file_path)


# 1. Counting unique values of each column
unique_values = data.nunique()
print("Unique values in each column:")
print(unique_values)

# 2. Format (data type) of each column
column_data_types = data.dtypes
print("\nData types of each column:")
print(column_data_types)

# 3. Identifying missing values
missing_values = data.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)

# 4. Fill missing values in numeric columns
# Select only numeric columns to apply mean fill
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns

# Fill missing values with the mean of each numeric column
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())

# If you want to fill categorical columns (like 'State' or 'Updated On') with a placeholder:
data['State'].fillna('Unknown', inplace=True)

# Print the updated dataset after filling missing values
print("\nDataset after filling missing values:")
print(data.head())
