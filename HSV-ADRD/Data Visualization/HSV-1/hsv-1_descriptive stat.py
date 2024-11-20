import pandas as pd

# Sample data for Descriptive Statistics
descriptive_data = {
    'Variable': ['Age (Mean, SD)', 'Male (%)', 'Female (%)', 'Hypertension (%)', 'Diabetes (%)', 'Cardiovascular Disease (%)'],
    'HSV-1 Infected': ['62.5, 10.7', '49.2', '50.8', '58.3', '22.1', '31.4'],
    'Non-Infected': ['62.5, 10.7', '49.3', '50.7', '45.7', '18.3', '25.9']
}

# Creating DataFrame
descriptive_df = pd.DataFrame(descriptive_data)

# Saving the table to a CSV file
descriptive_df.to_csv('descriptive_statistics.csv', index=False)

# Displaying the table
print("Descriptive Statistics Table:")
print(descriptive_df)

print("\nDescriptive Statistics Table has been saved as 'descriptive_statistics.csv'.")
