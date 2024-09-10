import pandas as pd
import matplotlib.pyplot as plt

# Manually loading the extracted data
data = {
    'Medication': [
        'Valacyclovir', 'Acyclovir', 'Gabapentin', 'Sertraline', 'Citalopram',
        'Pregabalin', 'Amitriptyline', 'Quetiapine', 'Valproic Acid', 'Risperidone',
        'Famciclovir', 'Donepezil', 'Carbamazepin', 'Memantine', 'Penciclovir'
    ],
    'Person Count': [726, 478, 239, 213, 88, 87, 84, 50, 31, 26, 16, 15, 12, 8, 8],
    'Pathway Percent': [54.5, 35.89, 17.94, 15.99, 6.61, 6.53, 6.31, 3.75, 2.33, 1.95, 1.2, 1.13, 0.9, 0.6, 0.6],
    'Cohort Percent': [37.31, 24.56, 12.28, 10.95, 4.52, 4.47, 4.32, 2.57, 1.59, 1.34, 0.82, 0.77, 0.62, 0.41, 0.41]
}

# Convert to a DataFrame
df = pd.DataFrame(data)

# Assigning colors to medications:
# Dementia/memory-related medications: Orange to red shades (Donepezil = red)
# HSV-related medications: Different colors (blue and green hues)
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
    '#8c564b',  # Donepezil (red/maroon)
    '#bcbd22',  # Carbamazepin (yellow)
    '#c5b0d5',  # Memantine (light purple)
    '#17becf'   # Penciclovir (cyan)
]

def add_labels_dynamic(ax, values, column_name):
    """
    Add percentage labels to the bars in the chart.
    The label will be placed inside the bar if the bar is long enough,
    otherwise, the label will be placed at the edge of the bar.
    """
    for i, value in enumerate(values):
        if value > 5:  # If bar is long enough, place the label inside the bar
            ax.text(value - 3, i, f'{value}%', va='center', ha='right', color='white')
        else:  # For shorter bars, place the label outside the bar
            ax.text(value + 1, i, f'{value}%', va='center', ha='left', color='black')

def add_labels_for_person_count(ax, values):
    """Add labels for Person Count (without percentage symbols)."""
    for i, value in enumerate(values):
        ax.text(value + 10, i, str(value), va='center', color='black')

# Plot 1: Person count for each medication (without percentage symbols)
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(df['Medication'], df['Person Count'], color=colors)
plt.xlabel('Person Count')
plt.ylabel('Medication Name')
plt.title('Medication Use by Person Count for HSV-1 Cohort')

# Add labels for Person Count
add_labels_for_person_count(ax, df['Person Count'])

# Invert y-axis for better visualization
ax.invert_yaxis()

# Show the plot with tight layout
plt.tight_layout()
plt.show()

# Plot 2: Pathway percent for each medication (dynamic placement of labels)
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(df['Medication'], df['Pathway Percent'], color=colors)
plt.xlabel('Pathway Percent')
plt.ylabel('Medication Name')
plt.title('Medication Use by Pathway Percent for HSV-1 Cohort')

# Add dynamic labels for Pathway Percent
add_labels_dynamic(ax, df['Pathway Percent'], 'Pathway Percent')

# Invert y-axis for better visualization
ax.invert_yaxis()

# Show the plot with tight layout
plt.tight_layout()
plt.show()

# Plot 3: Cohort percent for each medication (dynamic placement of labels)
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(df['Medication'], df['Cohort Percent'], color=colors)
plt.xlabel('Cohort Percent')
plt.ylabel('Medication Name')
plt.title('Medication Use by Cohort Percent for HSV-1 Cohort')

# Add dynamic labels for Cohort Percent
add_labels_dynamic(ax, df['Cohort Percent'], 'Cohort Percent')

# Invert y-axis for better visualization
ax.invert_yaxis()

# Show the plot with tight layout
plt.tight_layout()
plt.show()

# Displaying the DataFrame
print("Medication Data for HSV-1 Cohort:")
print(df)
