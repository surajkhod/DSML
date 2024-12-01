"""
Write a program to do: A dataset collected in a cosmetics shop showing
details of customers and whether or not they responded to a special offer
to buy a new lip-stick is shown in table below. (Use library commands)
According to the decision tree you have made from the previous training
data set, what is the decision for the test data: [Age > 35, Income =
Medium, Gender = Female, Marital Status = Married]?
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("/content/Lipstick.csv")

# Map categorical values to numeric values for decision tree compatibility
df['Age'] = df['Age'].map({'<21': 0, '21-35': 1, '>35': 2})
df['Income'] = df['Income'].map({'Low': 0, 'Medium': 1, 'High': 2})
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
df['Ms'] = df['Ms'].map({'Single': 0, 'Married': 1})
df['Buys'] = df['Buys'].map({'No': 0, 'Yes': 1})

# Separate features and target variable
X = df[['Age', 'Income', 'Gender', 'Ms']]
y = df['Buys']

# Train the Decision Tree model
model = DecisionTreeClassifier(criterion='entropy', random_state=42)
model.fit(X, y)

# Visualize the decision tree
plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=['Age', 'Income', 'Gender', 'Ms'],
          class_names=['No', 'Yes'], filled=True)
plt.title("Decision Tree Visualization")
plt.show()

# Test data
test_data = [[2, 1, 1, 1]]  # [Age > 35, Income = Medium, Gender = Female, Marital Status = Married]

# Make a prediction
prediction = model.predict(test_data)

# Display the result
if prediction[0] == 1:
    print("The decision for the test data is: Buys Yes")
else:
    print("The decision for the test data is: Buys No")
