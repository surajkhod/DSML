# Use the inbuilt dataset 'titanic'. The dataset contains 891 rows and
# contains information about the passengers who boarded the unfortunate
# Titanic ship. Write a code to check how the price of the ticket (column
# name: 'fare') for each passenger is distributed by plotting a histogram.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset from your local CSV file
titanic_data = pd.read_csv('/home/surajkhod/Coding/DSML/datasets/Titanic.csv')

# Plot a histogram for the 'Fare' column
plt.figure(figsize=(10, 6))
sns.histplot(data=titanic_data, x='Fare', bins=30, kde=True, color='blue')
plt.title("Distribution of Ticket Prices (Fare) on Titanic")
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
