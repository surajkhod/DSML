# Use House_Price prediction dataset. Provide summary statistics (mean,
# median, minimum, maximum, standard deviation) of variables (categorical
# vs quantitative) such as- For example, if categorical variable is age groups
# and quantitative variable is income, then provide summary statistics of
# income grouped by the age groups.

import pandas as pd

# Load the dataset
house_data = pd.read_csv("/home/surajkhod/Coding/DSML/datasets/House Data.csv")
# Check the columns in the dataset
print(house_data.columns)
# Remove currency symbols, commas, and other non-numeric characters from the 'price' column
house_data['price'] = house_data['price'].replace({r'[^\d.]': ''}, regex=True).astype(float)

# Choose categorical and quantitative columns
categorical_column = 'district'   # You can replace with another categorical column
quantitative_column = 'price'    # You can replace with another quantitative column

# Group the data by the categorical column and get summary statistics for the quantitative column
summary_stats = house_data.groupby(categorical_column)[quantitative_column].describe()

# To include specific summary statistics like mean, median, min, max, and standard deviation:
mean = house_data.groupby(categorical_column)[quantitative_column].mean()
median = house_data.groupby(categorical_column)[quantitative_column].median()
min_value = house_data.groupby(categorical_column)[quantitative_column].min()
max_value = house_data.groupby(categorical_column)[quantitative_column].max()
std_dev = house_data.groupby(categorical_column)[quantitative_column].std()

# Display the summary statistics
print("Summary Statistics (Mean, Median, Min, Max, Std Dev):\n")
print("Mean:\n", mean)
print("\nMedian:\n", median)
print("\nMinimum Value:\n", min_value)
print("\nMaximum Value:\n", max_value)
print("\nStandard Deviation:\n", std_dev)
