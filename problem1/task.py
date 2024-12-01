"""
Perform the following operations using Python on a data set : read data
from different formats(like csv, xls),indexing and selecting data, sort data,
describe attributes of data, checking data types of each column. (Use
Titanic Dataset).
"""

# -*- coding: utf-8 -*-
import pandas as pd

# Load the Titanic dataset provided by the user     
file_path = "/home/surajkhod/Coding/DSML/dsml/datasets/Titanic.csv"
titanic_df = pd.read_csv(file_path)

# Display the first few rows to understand its structure
titanic_df.head(), titanic_df.info()

# 1. Display the dataset structure and preview the first few rows
print("Dataset Preview:")
print(titanic_df.head())

# 2. Describe numeric statistics
print("\nDescriptive Statistics:")
print(titanic_df.describe())

# 3. Sorting data by 'Age' (ascending order)
sorted_df = titanic_df.sort_values(by='Age', ascending=True)
print("\nData Sorted by Age:")
print(sorted_df.head())

# 4. Checking data types of each column
print("\nData Types:")
print(titanic_df.dtypes)

# 5. Checking for null values
print("\nNull Value Check:")
print(titanic_df.isnull().sum())

# 6. Fill null values: numeric with mean, categorical with mode
numeric_columns = ['Age', 'Fare']
for column in numeric_columns:
    titanic_df[column] = titanic_df[column].fillna(titanic_df[column].mean())

categorical_columns = ['Cabin', 'Embarked']
for column in categorical_columns:
    titanic_df[column] = titanic_df[column].fillna(titanic_df[column].mode()[0])

# Check if null values remain after filling
print("\nNull Value Check After Filling:")
print(titanic_df.isnull().sum())

# 7. Converting 'Age' to integer
titanic_df['Age'] = titanic_df['Age'].astype(int)

# 8. Save the cleaned dataset to a new file
cleaned_file_path = "/home/surajkhod/Coding/DSML/dsml/problem1/Cleaned_Titanic.csv"
titanic_df.to_csv(cleaned_file_path, index=False)
print(f"\nCleaned dataset saved to: {cleaned_file_path}")

# 9. Final preview of the cleaned dataset
print("\nCleaned Dataset Preview:")
print(titanic_df.head())

