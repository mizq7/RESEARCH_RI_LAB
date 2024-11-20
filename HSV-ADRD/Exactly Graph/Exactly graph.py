import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create dataframes for each cohort
cohort_a = pd.DataFrame({
    'Cohort': 'A',
    'EventCohorts': ['Exactly 1', 'Exactly 0', 'Exactly 2', 'Exactly 3', 'Exactly 4', 'Exactly 5'],
    'PathwayPercent': [64.26, 0.00, 25.30, 7.13, 2.55, 0.75],
    'CohortPercent': [43.99, 31.55, 17.32, 4.88, 1.75, 0.51]
})

cohort_b = pd.DataFrame({
    'Cohort': 'B',
    'EventCohorts': ['Exactly 1', 'Exactly 0', 'Exactly 2', 'Exactly 3', 'Exactly 4', 'Exactly 5'],
    'PathwayPercent': [64.26, 0.00, 25.30, 7.13, 2.55, 0.75],
    'CohortPercent': [43.99, 31.55, 17.32, 4.88, 1.75, 0.51]
})

cohort_c = pd.DataFrame({
    'Cohort': 'C',
    'EventCohorts': ['Exactly 1', 'Exactly 0', 'Exactly 2', 'Exactly 3', 'Exactly 4', 'Exactly 5'],
    'PathwayPercent': [75.63, 0.00, 17.99, 4.45, 1.50, 0.43],
    'CohortPercent': [47.59, 37.08, 11.32, 2.80, 0.94, 0.27]
})

cohort_d = pd.DataFrame({
    'Cohort': 'D',
    'EventCohorts': ['Exactly 1', 'Exactly 0', 'Exactly 2', 'Exactly 3', 'Exactly 4', 'Exactly 5'],
    'PathwayPercent': [75.63, 0.00, 17.99, 4.45, 1.50, 0.43],
    'CohortPercent': [47.59, 37.08, 11.32, 2.80, 0.94, 0.27]
})

# Combine all cohorts into a single dataframe
all_cohorts = pd.concat([cohort_a, cohort_b, cohort_c, cohort_d], ignore_index=True)

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 16))
fig.suptitle('HSV-1 Cohort Comparison: Pathway and Cohort Percentages', fontsize=16)

# Plot Pathway Percentages
sns.barplot(x='EventCohorts', y='PathwayPercent', hue='Cohort', data=all_cohorts, ax=ax1)
ax1.set_title('Pathway Percentages Across Cohorts')
ax1.set_xlabel('Event Cohorts')
ax1.set_ylabel('Pathway Percent')
ax1.legend(title='Cohort')
ax1.set_ylim(0, 100)

# Plot Cohort Percentages
sns.barplot(x='EventCohorts', y='CohortPercent', hue='Cohort', data=all_cohorts, ax=ax2)
ax2.set_title('Cohort Percentages Across Cohorts')
ax2.set_xlabel('Event Cohorts')
ax2.set_ylabel('Cohort Percent')
ax2.legend(title='Cohort')
ax2.set_ylim(0, 100)

# Rotate x-axis labels for better readability
for ax in [ax1, ax2]:
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

plt.tight_layout()
plt.savefig('HSV-1_Cohort_Comparison.png', dpi=300, bbox_inches='tight')
plt.show()