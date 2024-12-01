"""
 Use Iris flower dataset and perform following :
1. List down the features and their types (e.g., numeric, nominal)
available in the dataset. 2. Create a histogram for each feature in the
dataset to illustrate the feature distributions.
"""

import pandas as pd

# Load the uploaded dataset
file_path = '/content/IRIS.csv'
iris_data = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure
iris_data.head(), iris_data.info()
import matplotlib.pyplot as plt

# List of numeric columns for histogram plotting
numeric_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

# Create histograms
plt.figure(figsize=(12, 8))
for i, column in enumerate(numeric_columns, 1):
    plt.subplot(2, 2, i)
    plt.hist(iris_data[column], bins=15, color='skyblue', edgecolor='black')
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
