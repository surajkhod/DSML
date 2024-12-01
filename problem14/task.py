"""
 Use the covid_vaccine_statewise.csv dataset and perform the following
analytics.
A. Describe the dataset.
B. Number of Males vaccinated
C.. Number of females vaccinated
"""


import pandas as pd

# Load the dataset to examine its contents
file_path = '/content/Covid Vaccine Statewise.csv'
data = pd.read_csv(file_path)

# Display the first few rows and summary info for understanding
data_info = data.info()
data_head = data.head()
data_info, data_head
# Summing up male and female doses administered across all rows (national-level totals)
total_male_vaccinated = data["Male (Doses Administered)"].sum()
total_female_vaccinated = data["Female (Doses Administered)"].sum()

total_male_vaccinated, total_female_vaccinated
