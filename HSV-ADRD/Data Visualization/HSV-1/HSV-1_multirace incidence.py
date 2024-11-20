import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data representing the percentage of patients by the number of races identified
data = {
    'Number of Races': ['No Race Assigned', 'Single Race', 'Two Races', 'Three Races', 'Four Races', 'Five Races', 'Six Races'],
    'Percentage of Patients': [18.83, 75.85, 3.64, 1.20, 0.44, 0.05, 0.01]
}

df = pd.DataFrame(data)

# Sort data for visualization
df = df.sort_values('Percentage of Patients')

# Create a horizontal bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='Percentage of Patients', y='Number of Races', data=df, palette='Blues_d')

plt.xlabel('Percentage of Patients (%)')
plt.ylabel('Number of Race Categories Identified')
plt.title('Figure 6. Distribution of Patients by Number of Race Categories')

# Annotate bars with percentage values
for index, value in enumerate(df['Percentage of Patients']):
    plt.text(value + 0.1, index, f'{value}%', va='center')

plt.tight_layout()
plt.show()
