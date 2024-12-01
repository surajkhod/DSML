"""
Write a program to do: A dataset collected in a cosmetics shop showing
details of customers and whether or not they responded to a special offer
to buy a new lip-stick is shown in table below. (Use library commands)
According to the decision tree you have made from the previous training
data set, what is the decision for the test data: [Age < 21, Income = Low,
Gender = Female, Marital Status = Married]?
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

df = pd.read_csv('/Database.csv')

print(df.head())

df['Age'] = df['Age'].map({'<21': 0, '21-35': 1, '>35': 2})
df['Income'] = df['Income'].map({'Low': 0, 'Medium': 1, 'High': 2})
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
df['Ms'] = df['Ms'].map({'Single': 0, 'Married': 1})
df['Buys'] = df['Buys'].map({'No': 0, 'Yes': 1})

print(df.head())

X = df[['Age', 'Income', 'Gender', 'Ms']]
y = df['Buys']

model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)

plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=['Age', 'Income', 'Gender', 'Ms'],
          class_names=['No', 'Yes'], filled=True)
plt.show()

test_sample = [[0, 0, 1, 1]]
prediction = model.predict(test_sample)

if prediction[0] == 1:
    print("The decision for the test data is: Buys Yes")
else:
    print("The decision for the test data is: Buys No")
