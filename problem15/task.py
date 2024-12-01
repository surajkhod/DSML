"""
Use the dataset 'titanic'. The dataset contains 891 rows and contains
information about the passengers who boarded the unfortunate Titanic
ship. Use the Seaborn library to see if we can find any patterns in the data.
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset('titanic')

data

data['age'] = data['age'].fillna(np.mean(data['age']))
data['deck'] = data['deck'].fillna(data['deck'].mode()[0])
data['embarked'] = data['embarked'].fillna(data['embarked'].mode()[0])
data['embark_town'] = data['embark_town'].fillna(data['embark_town'].mode()[0])

data.isnull().sum()

sns.countplot(data=data,x='survived')
plt.show()


sns.countplot(data=data,x='pclass')
plt.show()


sns.boxplot(data['age'])
plt.show()



sns.catplot(x = "sex", hue = "survived", kind = "count", data = data)
plt.title('Survival Count by gender')
plt.xlabel('Gender of passengers')
plt.ylabel('Count')
plt.show()

sns.countplot(x = 'pclass', hue = 'survived', data = data)
plt.title('Survival count by the passenger class')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.show()

sns.countplot(data = data, x = 'pclass', hue = 'sex')
plt.title('Number of passengers in each class')

sns.catplot(x = "sex", y = "age", data = data)

num = data.select_dtypes(include=['number'])
tc = num.corr()
sns.heatmap(tc, cmap = "YlGnBu")
plt.title('Correlation')
plt.show()


sns.histplot(data['fare'],bins=25, kde=True)
plt.title('Distribution of ticket fare')
plt.xlabel('Ticket Prices')
plt.ylabel('Frequency')
plt.show()

