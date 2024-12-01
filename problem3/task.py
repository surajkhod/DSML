"""
Perform the following operations using Python on the data set
House_Price Prediction dataset. Compute standard deviation, variance and
percentiles using separate commands, for each feature. Create a histogram
for each feature in the dataset to illustrate the feature distributions
"""

# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("/content/House Data.csv")

# Cleaning numerical columns
df['price'] = df['price'].str.replace('[^0-9,]', '', regex=True).str.replace(',', '').astype(float)
df['GrossSquareMeters'] = df['GrossSquareMeters'].str.replace(' m2', '', regex=True).astype(float)
df['NetSquareMeters'] = df['NetSquareMeters'].str.replace(' m2', '', regex=True).astype(float)
df['BuildingAge'] = df['BuildingAge'].str.extract('(\d+)', expand=False).astype(float)

# Clean additional columns
columns_to_clean = ['NumberOfBathrooms', 'NumberOfRooms', 'FloorLocation']
for col in columns_to_clean:
    df[col] = pd.to_numeric(df[col], errors='coerce')  # Handle non-numeric data

# Categorical encoding
categorical_columns = ['district', 'Category', 'UsingStatus', 'HeatingType', 'InsideTheSite']
df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)

# Select only numeric columns for analysis
numeric_df = df.select_dtypes(include=['number'])

# Summary statistics
print("Summary Statistics:")
print(numeric_df.describe())

# Compute specific statistics
print("\nMinimum values:")
print(numeric_df.min())

print("\nMaximum values:")
print(numeric_df.max())

print("\nMean values:")
print(numeric_df.mean())

print("\nStandard Deviation:")
print(numeric_df.std())

print("\nVariance:")
print(numeric_df.var())

# Compute percentiles
percentiles = [0.1, 0.3, 0.5, 0.7, 0.9]
percentile_results = numeric_df.quantile(percentiles)
print("\nPercentiles:")
print(percentile_results)

# Visualizing histograms for numerical features
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(18, 12))
axes = axes.flatten()

for i, col in enumerate(numeric_df.columns[:6]):  # Plot for the first 6 numeric columns
    axes[i].hist(numeric_df[col].dropna(), bins=20, edgecolor='black', color='skyblue')
    axes[i].set_title(f'Distribution of {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Frequency')

plt.tight_layout()
plt.show()

# Save cleaned dataset
numeric_df.to_csv("/content/Cleaned_House_Data.csv", index=False)
