import matplotlib.pyplot as plt
import pandas as pd

# Sample data for demographic characteristics
data = {
    'Gender': ['Female', 'Male', 'Transgender', 'Unknown'],
    'Count': [5121007, 4407721, 383, 41754]
}

ethnicity_data = {
    'Ethnicity': ['Hispanic', 'Not Hispanic', 'Missing/Refused'],
    'Count': [595213, 7147264, 1828879]
}

race_data = {
    'Race': ['American Indian/Alaska Native', 'Asian', 'Black/African American', 'Native Hawaiian/Pacific Islander',
             'Other', 'White', 'Multi-Race', 'Unknown'],
    'Count': [49134, 218978, 1095181, 20480, 584252, 6324433, 508863, 683]
}

# Convert to DataFrame
df_gender = pd.DataFrame(data)
df_ethnicity = pd.DataFrame(ethnicity_data)
df_race = pd.DataFrame(race_data)

# Create bar plots
plt.figure(figsize=(10, 5))
plt.bar(df_gender['Gender'], df_gender['Count'], color='lightblue')
plt.title('Distribution of Gender in IIS Patients')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(df_ethnicity['Ethnicity'], df_ethnicity['Count'], color='lightgreen')
plt.title('Distribution of Ethnicity in IIS Patients')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(12, 6))
plt.barh(df_race['Race'], df_race['Count'], color='lightcoral')
plt.title('Distribution of Race in IIS Patients')
plt.xlabel('Count')
plt.show()
