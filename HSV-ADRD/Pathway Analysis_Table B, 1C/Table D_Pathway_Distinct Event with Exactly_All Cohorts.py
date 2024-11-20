import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data for Exactly event cohorts across four cohorts
data = {
    'Cohort': ['Cohort A', 'Cohort B', 'Cohort C', 'Cohort D',
               'Cohort A', 'Cohort B', 'Cohort C', 'Cohort D',
               'Cohort A', 'Cohort B', 'Cohort C', 'Cohort D',
               'Cohort A', 'Cohort B', 'Cohort C', 'Cohort D',
               'Cohort A', 'Cohort B', 'Cohort C', 'Cohort D',
               'Cohort A', 'Cohort B', 'Cohort C', 'Cohort D'],
    'Event Cohort': ['Exactly 0', 'Exactly 0', 'Exactly 0', 'Exactly 0',
                     'Exactly 1', 'Exactly 1', 'Exactly 1', 'Exactly 1',
                     'Exactly 2', 'Exactly 2', 'Exactly 2', 'Exactly 2',
                     'Exactly 3', 'Exactly 3', 'Exactly 3', 'Exactly 3',
                     'Exactly 4', 'Exactly 4', 'Exactly 4', 'Exactly 4',
                     'Exactly 5', 'Exactly 5', 'Exactly 5', 'Exactly 5'],
    'Person Count': [614, 614, 1376, 1376,
                     856, 856, 1766, 1766,
                     337, 337, 420, 420,
                     95, 95, 104, 104,
                     34, 34, 35, 35,
                     10, 10, 10, 10],
    'Pathway Percent': [31.55, 31.55, 37.08, 37.08,
                        43.99, 43.99, 47.59, 47.59,
                        17.32, 17.32, 11.32, 11.32,
                        4.88, 4.88, 2.80, 2.80,
                        1.75, 1.75, 0.94, 0.94,
                        0.51, 0.51, 0.27, 0.27]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set the plot style
sns.set(style="whitegrid")

# Plotting Person Count for all four cohorts
plt.figure(figsize=(12, 8))
ax = sns.barplot(x='Person Count', y='Event Cohort', hue='Cohort', data=df)
plt.title('Person Count by Event Cohort Across Four Cohorts')

# Adding person count to the bars (excluding 0.00%)
for p in ax.patches:
    width = p.get_width()
    if width != 0:  # Exclude 0 counts from being displayed
        plt.text(width + 10, p.get_y() + p.get_height()/2, f'{int(width)}', va='center')

plt.show()

# Plotting Pathway Percent for all four cohorts
plt.figure(figsize=(12, 8))
ax = sns.barplot(x='Pathway Percent', y='Event Cohort', hue='Cohort', data=df)
plt.title('Pathway Percent by Distinct Event Cohort Across Four Cohorts')

# Adding pathway percentage to the bars (excluding 0.00%)
for p in ax.patches:
    width = p.get_width()
    if width > 0.0:  # Exclude 0.00% from being displayed
        plt.text(width + 0.1, p.get_y() + p.get_height()/2, f'{width:.2f}%', va='center')

plt.show()
