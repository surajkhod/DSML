"""
Perform the following operations using Python on the Telecom_Churn
dataset. Compute and display summary statistics for each feature available
in the dataset using separate commands for each statistic. (e.g. minimum
value, maximum value, mean, range, standard deviation, variance and
percentiles).
"""
import pandas as pd
# Load the Telecom Churn dataset
telecom_churn_path = "/home/surajkhod/Coding/DSML/dsml/datasets/Telecom Churn.csv"
telecom_df = pd.read_csv(telecom_churn_path)

# Display the first few rows and dataset info to understand its structure
telecom_df.head(), telecom_df.info()
# Selecting only numeric columns for statistical analysis
numeric_features = telecom_df.select_dtypes(include=['float64', 'int64']).columns

# Initialize a dictionary to hold statistics
statistics = {}

# Compute and store statistics for each numeric feature
for feature in numeric_features:
    stats = {
        "min": telecom_df[feature].min(),
        "max": telecom_df[feature].max(),
        "mean": telecom_df[feature].mean(),
        "range": telecom_df[feature].max() - telecom_df[feature].min(),
        "std_dev": telecom_df[feature].std(),
        "variance": telecom_df[feature].var(),
        "25th_percentile": telecom_df[feature].quantile(0.25),
        "50th_percentile": telecom_df[feature].quantile(0.50),
        "75th_percentile": telecom_df[feature].quantile(0.75),
    }
    statistics[feature] = stats

# Display computed statistics for each numeric feature

# Specify the feature for which you want to display statistics
selected_feature = 'total day charge'  # Replace with your desired column name

# Check if the feature exists in the statistics dictionary
if selected_feature in statistics:
    stats = statistics[selected_feature]
    print(f"Statistics for feature: {selected_feature}")
    print(f"Minimum Value: {stats['min']}")
    print(f"Maximum Value: {stats['max']}")
    print(f"Mean: {stats['mean']:.2f}")
    print(f"Range: {stats['range']}")
    print(f"Standard Deviation: {stats['std_dev']:.2f}")
    print(f"Variance: {stats['variance']:.2f}")
    print(f"25th Percentile: {stats['25th_percentile']:.2f}")
    print(f"50th Percentile (Median): {stats['50th_percentile']:.2f}")
    print(f"75th Percentile: {stats['75th_percentile']:.2f}")
else:
    print(f"Feature '{selected_feature}' not found in the dataset or statistics.")
