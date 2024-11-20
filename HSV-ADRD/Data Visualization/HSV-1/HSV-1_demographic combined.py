import matplotlib.pyplot as plt
import pandas as pd

# Sample data for demographic characteristics
gender_data = {
    'Gender': ['Female', 'Male', 'Transgender', 'Unknown'],
    'Count': [5121007, 4407721, 383, 41754]
}

ethnicity_data = {
    'Ethnicity': ['Hispanic', 'Not Hispanic', 'Missing/Refused'],
    'Count': [595213, 7147264, 1828879]
}

race_data = {
    'Race': ['American Indian/Alaska Native', 'Asian', 'Black/African American',
             'Native Hawaiian/Pacific Islander', 'Other', 'White', 'Multi-Race', 'Unknown'],
    'Count': [49134, 218978, 1095181, 20480, 584252, 6324433, 508863, 683]
}

# Convert to DataFrame
df_gender = pd.DataFrame(gender_data)
df_ethnicity = pd.DataFrame(ethnicity_data)
df_race = pd.DataFrame(race_data)

# Create a single figure with three horizontal subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 6))  # 1 row, 3 columns

# Gender bar plot
axes[0].bar(df_gender['Gender'], df_gender['Count'], color='lightblue')
axes[0].set_title('(a) Gender Distribution')
axes[0].set_ylabel('Count')

# Ethnicity bar plot
axes[1].bar(df_ethnicity['Ethnicity'], df_ethnicity['Count'], color='lightgreen')
axes[1].set_title('(b) Ethnicity Distribution')

# Race bar plot (horizontal)
axes[2].barh(df_race['Race'], df_race['Count'], color='lightcoral')
axes[2].set_title('(c) Race Distribution')
axes[2].set_xlabel('Count')

# Adjust layout
plt.tight_layout()
plt.show()
