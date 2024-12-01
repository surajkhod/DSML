"""
Use Iris flower dataset and perform following :
1. Create a box plot for each feature in the dataset.
2. Identify and discuss distributions and identify outliers from them.
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

# Create box plots for each numeric feature
plt.figure(figsize=(12, 8))
for i, column in enumerate(numeric_columns, 1):
    plt.subplot(2, 2, i)
    plt.boxplot(iris_data[column], patch_artist=True, boxprops=dict(facecolor='lightblue'))
    plt.title(f'Box Plot of {column}')
    plt.ylabel(column)

plt.tight_layout()
plt.show()
