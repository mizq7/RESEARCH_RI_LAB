import pandas as pd  # Import pandas
import matplotlib.pyplot as plt

# Sample data for Multi-Race Identification
multi_race_data = {
    'Race Category': ['Single Race', 'Two Races', 'Three Races', 'Four Races', 'Five Races', 'Six Races', 'No Race Info'],
    'Percentage': [76.17, 5.32, 0.44, 0.21, 0.02, 0.004, 18.83]
}

# Convert to DataFrame
df_multi_race = pd.DataFrame(multi_race_data)

# Stacked bar plot
plt.figure(figsize=(12, 6))
plt.bar(df_multi_race['Race Category'], df_multi_race['Percentage'], color='lightsteelblue')
plt.title('Incidence of Multi-Race Identification in IIS Data')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=45)
plt.show()
