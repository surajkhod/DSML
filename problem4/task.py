"""
Write a program to do: A dataset collected in a cosmetics shop showing
details of customers and whether or not they responded to a special offer
to buy a new lip-stick is shown in table below. (Implement step by step
using commands - Dont use library) Use this dataset to build a decision
tree, with Buys as the target variable, to help in buying lipsticks in the
future. Find the root node of the decision tree.
"""

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("/content/Lipstick.csv")

# Convert categorical features to numeric values for decision tree compatibility
# Adjust these mappings according to your dataset
df['Age'] = df['Age'].map({'<21': 0, '21-35': 1, '>35': 2})
df['Income'] = df['Income'].map({'Low': 0, 'Medium': 1, 'High': 2})
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
df['Ms'] = df['Ms'].map({'Single': 0, 'Married': 1})
df['Buys'] = df['Buys'].map({'No': 0, 'Yes': 1})

# Helper functions for entropy and information gain
def entropy(data):
    """Calculate entropy of the target variable."""
    values, counts = np.unique(data, return_counts=True)
    probabilities = counts / len(data)
    return -np.sum(probabilities * np.log2(probabilities))

def information_gain(data, split_attribute, target):
    """Calculate information gain for a specific attribute."""
    total_entropy = entropy(data[target])
    values, counts = np.unique(data[split_attribute], return_counts=True)

    weighted_entropy = 0
    for i in range(len(values)):
        subset = data[data[split_attribute] == values[i]]
        weighted_entropy += (counts[i] / len(data)) * entropy(subset[target])
    
    return total_entropy - weighted_entropy

# Calculate overall entropy
target_entropy = entropy(df['Buys'])
print(f"Entropy of the target variable (Buys): {target_entropy}")

# Calculate information gain for each attribute
attributes = ['Age', 'Income', 'Gender', 'Ms']
info_gains = {attr: information_gain(df, attr, 'Buys') for attr in attributes}

print("\nInformation Gain for each attribute:")
for attr, gain in info_gains.items():
    print(f"{attr}: {gain}")

# Find the root node (attribute with the highest information gain)
root_node = max(info_gains, key=info_gains.get)
print(f"\nThe root node is: {root_node}")

# Example of splitting data based on root node
split_values = df[root_node].unique()
for value in split_values:
    subset = df[df[root_node] == value]
    print(f"\nSubset for {root_node} = {value}:")
    print(subset)

# Visualization using DecisionTreeClassifier
X = df[['Age', 'Income', 'Gender', 'Ms']]
y = df['Buys']

# Fit the model
model = DecisionTreeClassifier(criterion='entropy', random_state=42)
model.fit(X, y)

# Plot the decision tree
plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=['Age', 'Income', 'Gender', 'Ms'],
          class_names=['No', 'Yes'], filled=True)
plt.title("Decision Tree Visualization")
plt.show()
