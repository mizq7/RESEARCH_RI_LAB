import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create dataframes for each cohort (same as before)
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

# Create a figure with subplots
fig = plt.figure(figsize=(20, 15))
fig.suptitle('HSV-1 Cohort Comparison: Pathway and Cohort Percentages', fontsize=20)

# Create pie charts for each cohort
cohorts = ['A', 'B', 'C', 'D']
for i, cohort in enumerate(cohorts):
    ax = fig.add_subplot(2, 4, i + 1)
    data = all_cohorts[all_cohorts['Cohort'] == cohort]
    wedges, texts, autotexts = ax.pie(data['CohortPercent'], autopct='%1.1f%%', startangle=90, pctdistance=0.85)
    ax.set_title(f'Cohort {cohort}')

    # Add legend
    ax.legend(wedges, data['EventCohorts'], title="Event Cohorts", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Create heatmap for pathway percentages
ax_heatmap = fig.add_subplot(2, 1, 2)
heatmap_data = all_cohorts.pivot(index='Cohort', columns='EventCohorts', values='PathwayPercent')
sns.heatmap(heatmap_data, annot=True, fmt='.2f', cmap='YlOrRd', ax=ax_heatmap)
ax_heatmap.set_title('Pathway Percentages Across Cohorts')
ax_heatmap.set_ylabel('Cohort')
ax_heatmap.set_xlabel('Event Cohorts')

plt.tight_layout()
plt.savefig('HSV-1_Cohort_Comparison_Pie_Heatmap.png', dpi=300, bbox_inches='tight')
plt.show()