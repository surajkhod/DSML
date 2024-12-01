To build the decision tree. The goal is to determine the root
node by maximizing information gain for the "Buys" target
variable.

1. Dataset and Attribute Description:
- Attributes:
- Age: <21, 21–35, >35
- Income: Low, Medium, High
- Gender: Male, Female
- Marital Status: Single, Married
- Target variable: Buys (Yes/No)
2. Steps for Building the Decision Tree:
2.1 Compute Entropy for the Entire Dataset
Entropy (E(S)) formula:

where (p ) is the proportion of class (i) in the dataset.

i

2.2 Compute Information Gain for Each Attribute
Information Gain (IG) measures how well an attribute
separates data into target classes. The formula for Information
Gain is:

(E(S )): Entropy of the subset for a given attribute value (v).



- (S ): Subset of data where attribute (A) has value (v).
v

2.3 Select the Root Node
- The attribute with the highest information gain becomes the
root node.
- Repeat this process recursively for the remaining nodes until
the tree is complete or no further splitting is possible.

---

Below is a simple Python algorithm to determine the root node
and predict for test data.
Step 1: Calculate Entropy for the Entire Dataset
Step 2: Compute Information Gain for Each Attribute
Repeat the process for Income, Gender, and Marital Status, and
compare the Information Gains. The attribute with the highest
gain becomes the root node.

Decision Tree Prediction for Test Data

Given test data:
[Age < 21, Income = Low, Gender = Female, Marital Status =
Married]
From the dataset:
- If Age < 21 and Income = Low, the outcome is Buys = Yes.

Thus, the decision for the test data is Yes.
