import matplotlib.pyplot as plt
import numpy as np

# Medication data and corresponding values extracted from the table
medications = ['Valacyclovir', 'Acyclovir', 'Gabapentin', 'Sertraline', 'Citalopram',
               'Pregabalin', 'Amitriptyline', 'Quetiapine', 'Valproic Acid', 'Risperidone',
               'Famciclovir', 'Donepezil', 'Carbamazepin', 'Memantine', 'Penciclovir']
person_count = [726, 478, 239, 213, 88, 87, 84, 50, 31, 26, 16, 15, 12, 8, 8]
pathway_percent = [54.50, 35.89, 17.94, 15.99, 6.61, 6.53, 6.31, 3.75, 2.33, 1.95, 1.20, 1.13, 0.90, 0.60, 0.60]
cohort_percent = [37.31, 24.56, 12.28, 10.95, 4.52, 4.47, 4.32, 2.57, 1.59, 1.34, 0.82, 0.77, 0.62, 0.41, 0.41]

# Sort data in descending order for proper visualization (largest at the top)
sorted_person_count = sorted(zip(person_count, medications), reverse=True)
sorted_pathway_percent = sorted(zip(pathway_percent, medications), reverse=True)
sorted_cohort_percent = sorted(zip(cohort_percent, medications), reverse=True)

# Extract sorted values
person_count_sorted, medications_person_sorted = zip(*sorted_person_count)
pathway_percent_sorted, medications_pathway_sorted = zip(*sorted_pathway_percent)
cohort_percent_sorted, medications_cohort_sorted = zip(*sorted_cohort_percent)

# Create a color palette (each bar has a unique color)
colors = plt.cm.tab20(np.linspace(0, 1, len(medications)))  # 15 unique colors

# Plot 1: Horizontal bar chart for Person Count
fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.barh(medications_person_sorted, person_count_sorted, color=colors)
ax.set_xlabel('Person Count', fontsize=12)
ax.set_ylabel('Medication Name', fontsize=12)
ax.set_title('Person Count for Each Medication', fontsize=14)

# Display values on the bars
for bar, value in zip(bars1, person_count_sorted):
    width = bar.get_width()
    ax.text(width + 10, bar.get_y() + bar.get_height()/2, f'{value}', va='center')

# Invert y-axis for proper ordering
ax.invert_yaxis()

# Show the first plot
plt.tight_layout()
plt.show()

# Plot 2: Horizontal bar chart for Pathway Percent
fig, ax = plt.subplots(figsize=(10, 6))
bars2 = ax.barh(medications_pathway_sorted, pathway_percent_sorted, color=colors)
ax.set_xlabel('Pathway Percent', fontsize=12)
ax.set_ylabel('Medication Name', fontsize=12)
ax.set_title('Pathway Percent for Each Medication', fontsize=14)

# Display values on the bars
for bar, value in zip(bars2, pathway_percent_sorted):
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2, f'{value}%', va='center')

# Invert y-axis for proper ordering
ax.invert_yaxis()

# Show the second plot
plt.tight_layout()
plt.show()

# Plot 3: Horizontal bar chart for Cohort Percent
fig, ax = plt.subplots(figsize=(10, 6))
bars3 = ax.barh(medications_cohort_sorted, cohort_percent_sorted, color=colors)
ax.set_xlabel('Cohort Percent', fontsize=12)
ax.set_ylabel('Medication Name', fontsize=12)
ax.set_title('Cohort Percent for Each Medication', fontsize=14)

# Display values on the bars
for bar, value in zip(bars3, cohort_percent_sorted):
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2, f'{value}%', va='center')

# Invert y-axis for proper ordering
ax.invert_yaxis()

# Show the third plot
plt.tight_layout()
plt.show()
