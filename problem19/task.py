# 19. Write a Python program to display some basic statistical details like
# percentile, mean, standard deviation etc (Use python and pandas
# commands) the species of ‘Iris-setosa’, ‘Iris-versicolor’ and ‘Iris-versicolor’
# of iris.csv dataset.


import pandas as pd

# Load the Iris dataset
iris_data = pd.read_csv("/home/surajkhod/Coding/DSML/datasets/IRIS.csv")


# Display the first few rows to verify the structure
print("Dataset Preview:")
print(iris_data.head())

# Group the data by the correct column name ('species')
species_group = iris_data.groupby('species')

# Calculate and display statistical details for each species
print("\nStatistical Details by Species:")
for species, group in species_group:
    print(f"\nSpecies: {species}")
    print(group.describe())

