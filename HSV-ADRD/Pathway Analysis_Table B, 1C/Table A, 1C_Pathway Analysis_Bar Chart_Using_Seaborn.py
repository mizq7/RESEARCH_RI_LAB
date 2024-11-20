import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Medication data and corresponding values extracted from the table
medications = ['Valacyclovir', 'Acyclovir', 'Gabapentin', 'Sertraline', 'Citalopram',
               'Pregabalin', 'Amitriptyline', 'Quetiapine', 'Valproic Acid', 'Risperidone',
               'Famciclovir', 'Donepezil', 'Carbamazepin', 'Memantine', 'Penciclovir']
person_count = [726, 478, 239, 213, 88, 87, 84, 50, 31, 26, 16, 15, 12, 8, 8]
pathway_percent = [54.50, 35.89, 17.94, 15.99, 6.61, 6.53, 6.31, 3.75, 2.33, 1.95, 1.20, 1.13, 0.90, 0.60, 0.60]
cohort_percent = [37.31, 24.56, 12.28, 10.95, 4.52, 4.47, 4.32, 2.57, 1.59, 1.34, 0.82, 0.77, 0.62, 0.41, 0.41]

# Create DataFrames for Seaborn
data_person = pd.DataFrame({'Medication': medications, 'Person Count': person_count}).sort_values(by='Person Count', ascending=False)
data_pathway = pd.DataFrame({'Medication': medications, 'Pathway Percent': pathway_percent}).sort_values(by='Pathway Percent', ascending=False)
data_cohort = pd.DataFrame({'Medication': medications, 'Cohort Percent': cohort_percent}).sort_values(by='Cohort Percent', ascending=False)

# Set the Seaborn style for attractive plots
sns.set(style="whitegrid")

# Plot 1: Horizontal bar chart for Person Count using Seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='Person Count', y='Medication', data=data_person, palette='viridis')
plt.title('Person Count for Each Medication', fontsize=14)
for index, value in enumerate(data_person['Person Count']):
    plt.text(value + 10, index, str(value), va='center')
plt.tight_layout()
plt.show()

# Plot 2: Horizontal bar chart for Pathway Percent using Seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='Pathway Percent', y='Medication', data=data_pathway, palette='magma')
plt.title('Pathway Percent for Each Medication', fontsize=14)
for index, value in enumerate(data_pathway['Pathway Percent']):
    plt.text(value + 1, index, f'{value}%', va='center')
plt.tight_layout()
plt.show()

# Plot 3: Horizontal bar chart for Cohort Percent using Seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='Cohort Percent', y='Medication', data=data_cohort, palette='coolwarm')
plt.title('Cohort Percent for Each Medication', fontsize=14)
for index, value in enumerate(data_cohort['Cohort Percent']):
    plt.text(value + 1, index, f'{value}%', va='center')
plt.tight_layout()
plt.show()
