"""
With reference to Table , obtain the Frequency table for the
attribute age. From the frequency table you have obtained, calculate the
information gain of the frequency table while splitting on Age. (Use step
by step Python/Pandas commands)
"""

import pandas as pd
import numpy as np

# Recreating the data from the image into a Pandas DataFrame
data = {
    "Age": [
        "Young", "Young", "Middle", "Old", "Old", "Old", "Middle", "Young",
        "Young", "Old", "Young", "Middle", "Middle", "Old"
    ],
    "Income": [
        "High", "High", "High", "Medium", "Low", "Low", "Low", "Medium",
        "Low", "Medium", "Medium", "Medium", "High", "Medium"
    ],
    "Married": [
        "No", "No", "Yes", "No", "Yes", "Yes", "No", "No",
        "Yes", "Yes", "Yes", "Yes", "No", "No"
    ],
    "Health": [
        "Fair", "Good", "Fair", "Fair", "Fair", "Good", "Fair", "Fair",
        "Fair", "Fair", "Good", "Good", "Fair", "Good"
    ],
    "Class": [
        "No", "No", "Yes", "Yes", "Yes", "Yes", "No", "No",
        "No", "Yes", "No", "Yes", "Yes", "No"
    ]
}

df = pd.DataFrame(data)

# Step 1: Frequency table for "Age"
freq_table = df["Age"].value_counts().reset_index()
freq_table.columns = ["Age", "Frequency"]
freq_table



# Function to calculate entropy
def calculate_entropy(series):
    probs = series.value_counts(normalize=True)
    entropy = -np.sum(probs * np.log2(probs))
    return entropy

# Step 2: Calculate total entropy of the dataset based on "Class"
total_entropy = calculate_entropy(df["Class"])

# Step 3: Calculate entropy for each subset split by "Age"
subgroup_entropy = {}
for age_group in df["Age"].unique():
    subset = df[df["Age"] == age_group]
    entropy = calculate_entropy(subset["Class"])
    subgroup_entropy[age_group] = entropy

# Step 4: Weighted entropy of splits
weighted_entropy = sum(
    (df[df["Age"] == age_group].shape[0] / df.shape[0]) * entropy
    for age_group, entropy in subgroup_entropy.items()
)

# Step 5: Information Gain
information_gain = total_entropy - weighted_entropy

total_entropy, subgroup_entropy, weighted_entropy, information_gain

