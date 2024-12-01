"""
Use the covid_vaccine_statewise.csv dataset and perform the following
analytics.
a. Describe the dataset
b. Number of persons state wise vaccinated for first dose in India
c. Number of persons state wise vaccinated for second dose in India
"""
import pandas as pd

# Load the dataset to examine its contents
file_path = '/content/Covid Vaccine Statewise.csv'
data = pd.read_csv(file_path)

# Display the first few rows and summary info for understanding
data_info = data.info()
data_head = data.head()
data_info, data_head

# Summarizing state-wise first and second dose counts
first_dose_statewise = data.groupby("State")["First Dose Administered"].sum()
second_dose_statewise = data.groupby("State")["Second Dose Administered"].sum()

# Converting results to a DataFrame for clarity
dose_summary = pd.DataFrame({
    "First Dose Administered": first_dose_statewise,
    "Second Dose Administered": second_dose_statewise
}).reset_index()

dose_summary.sort_values(by="State", inplace=True)  # Sorting by state for better readability
dose_summary
