import pandas as pd
import matplotlib.pyplot as plt

# Data from Table D, 1C
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

# Create a DataFrame
df = pd.DataFrame(data)

# Assign colors to medications
colors = [
    '#1f77b4', '#2ca02c', '#ff7f0e', '#ffbb78', '#ff9896', '#2ca02c', '#d62728',
    '#ffbb78', '#c49c94', '#98df8a', '#aec7e8', '#8c564b', '#bcbd22', '#c5b0d5', '#17becf', '#8c564b'
]

def add_labels(ax, values, percentage=False):
    """Add labels on each bar."""
    for i, value in enumerate(values):
        label = f"{value}%" if percentage else f"{value}"
        ax.text(value + 1, i, label, va='center')

# Plot 1: Person Count for each medication
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(df['Medication'], df['Person Count'], color=colors)
ax.set_xlabel('Person Count')
ax.set_ylabel('Medication')
ax.set_title('Person Count for Each Medication')
add_labels(ax, df['Person Count'])
ax.invert_yaxis()
plt.tight_layout()
plt.show()

# Plot 2: Pathway Percent for each medication
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(df['Medication'], df['Pathway Percent'], color=colors)
ax.set_xlabel('Pathway Percent')
ax.set_ylabel('Medication')
ax.set_title('Pathway Percent for Each Medication')
add_labels(ax, df['Pathway Percent'], percentage=True)
ax.invert_yaxis()
plt.tight_layout()
plt.show()

# Plot 3: Cohort Percent for each medication
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(df['Medication'], df['Cohort Percent'], color=colors)
ax.set_xlabel('Cohort Percent')
ax.set_ylabel('Medication')
ax.set_title('Cohort Percent for Each Medication')
add_labels(ax, df['Cohort Percent'], percentage=True)
ax.invert_yaxis()
plt.tight_layout()
plt.show()
