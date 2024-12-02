# Perform Data Cleaning, Data transformation using Python on any data
# set.


import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Step 1: Load the dataset
file_path = 'F:\\ty sem I\\DSML\\PR\\IRIS.csv'  # Update with the file location
iris_data = pd.read_csv(file_path)

# Step 2: Check and handle missing values
# Identify missing values
print("Missing Values Before Cleaning:")
print(iris_data.isnull().sum())

# Fill missing values (if any) using mean (for numeric) or mode (for categorical)
iris_data.fillna({
    'sepal_length': iris_data['sepal_length'].mean(),
    'sepal_width': iris_data['sepal_width'].mean(),
    'petal_length': iris_data['petal_length'].mean(),
    'petal_width': iris_data['petal_width'].mean(),
    'species': iris_data['species'].mode()[0]
}, inplace=True)

print("\nMissing Values After Cleaning:")
print(iris_data.isnull().sum())

# Step 3: Standardize column names
iris_data.columns = [col.strip().lower().replace(' ', '_') for col in iris_data.columns]

# Step 4: Normalize numeric columns
scaler = MinMaxScaler()
numeric_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
iris_data[numeric_columns] = scaler.fit_transform(iris_data[numeric_columns])

print("\nData After Normalization:")
print(iris_data.head())

# Step 5: Encode categorical variables
encoder = LabelEncoder()
iris_data['species_encoded'] = encoder.fit_transform(iris_data['species'])

print("\nSpecies Encoding:")
print(iris_data[['species', 'species_encoded']].drop_duplicates())

# Step 6: Add derived features
iris_data['sepal_area'] = iris_data['sepal_length'] * iris_data['sepal_width']
iris_data['petal_area'] = iris_data['petal_length'] * iris_data['petal_width']

print("\nData with Derived Features:")
print(iris_data.head())

# Step 7: Outlier Detection (Flagging)
# Flag rows with unusually large/small values in numeric columns
thresholds = {col: (iris_data[col].quantile(0.25), iris_data[col].quantile(0.75)) for col in numeric_columns}
outliers = {}
for col, (q1, q3) in thresholds.items():
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outliers[col] = iris_data[(iris_data[col] < lower) | (iris_data[col] > upper)]

print("\nOutlier Summary:")
for col, df_outliers in outliers.items():
    print(f"Outliers in {col}:")
    print(df_outliers)
