import pandas as pd
import matplotlib.pyplot as plt

# Manually loading the extracted data from Table C, 1C
data = {
    'Medication': [
        'Valacyclovir', 'Acyclovir', 'Gabapentin', 'Sertraline', 'Citalopram',
        'Pregabalin', 'Amitriptyline', 'Quetiapine', 'Valproic Acid', 'Risperidone',
        'Famciclovir', 'Donepezil', 'Carbamazepin', 'Memantine', 'Penciclovir', 'Rivastigmine'
    ],
    'Person Count': [1403, 749, 283, 253, 107, 111, 109, 64, 39, 28, 27, 18, 15, 12, 11, 1],
    'Pathway Percent': [60.09, 32.08, 12.12, 10.84, 4.58, 4.75, 4.67, 2.74, 1.67, 1.20, 1.16, 0.77, 0.64, 0.51, 0.47, 0.04],
    'Cohort Percent': [37.81, 20.18, 7.63, 6.82, 2.88, 2.99, 2.94, 1.72, 1.05, 0.75, 0.73, 0.49, 0.40, 0.32, 0.30, 0.03]
}

# Convert to a DataFrame
df = pd.DataFrame(data)

# Assigning colors to medications:
colors = [
    '#1f77b4',  # Valacyclovir (blue)
    '#2ca02c',  # Acyclovir (green)
    '#ff7f0e',  # Gabapentin (orange)
    '#ffbb78',  # Sertraline (light orange)
    '#ff9896',  # Citalopram (light red-orange)
    '#2ca02c',  # Pregabalin (green)
    '#d62728',  # Amitriptyline (dark orange)
    '#ffbb78',  # Quetiapine (light orange)
    '#c49c94',  # Valproic Acid (brown)
    '#98df8a',  # Risperidone (light green)
    '#aec7e8',  # Famciclovir (light blue)
    '#8c564b',  # Donepezil (red)
    '#bcbd22',  # Carbamazepin (yellow)
    '#c5b0d5',  # Memantine (light purple)
    '#17becf',  # Penciclovir (cyan)
    '#8c564b'   # Rivastigmine (red)
]

# Plot 1: Person count for each medication (without percentage symbols)
fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.barh(df['Medication'], df['Person Count'], color=colors)
plt.xlabel('Person Count')
plt.ylabel('Medication Name')
plt.title('Medication Use by Person Count for HSV-1 Cohort')

# Add labels for Person Count
for i, value in enumerate(df['Person Count']):
    plt.text(value + 10, i, str(value), va='center')

# Invert y-axis for proper ordering
ax.invert_yaxis()

# Show the first plot
plt.tight_layout()
plt.show()

# Plot 2: Pathway percent for each medication
fig, ax = plt.subplots(figsize=(10, 6))
bars2 = ax.barh(df['Medication'], df['Pathway Percent'], color=colors)
plt.xlabel('Pathway Percent')
plt.ylabel('Medication Name')
plt.title('Medication Use by Pathway Percent for HSV-1 Cohort')

# Add labels for Pathway Percent
for i, value in enumerate(df['Pathway Percent']):
    plt.text(value + 1, i, f'{value}%', va='center')

# Invert y-axis for proper ordering
ax.invert_yaxis()

# Show the second plot
plt.tight_layout()
plt.show()

# Plot 3: Cohort percent for each medication
fig, ax = plt.subplots(figsize=(10, 6))
bars3 = ax.barh(df['Medication'], df['Cohort Percent'], color=colors)
plt.xlabel('Cohort Percent')
plt.ylabel('Medication Name')
plt.title('Medication Use by Cohort Percent for HSV-1 Cohort')

# Add labels for Cohort Percent
for i, value in enumerate(df['Cohort Percent']):
    plt.text(value + 1, i, f'{value}%', va='center')

# Invert y-axis for proper ordering
ax.invert_yaxis()

# Show the third plot
plt.tight_layout()
plt.show()