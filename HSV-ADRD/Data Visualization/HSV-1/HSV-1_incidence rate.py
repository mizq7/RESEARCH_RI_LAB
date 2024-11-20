import pandas as pd
import matplotlib.pyplot as plt

# Sample data for Incidence Rate Analysis
incidence_data = {
    'Outcome': ['Mild Cognitive Impairment (MCI)', 'Alzheimer’s Disease and Related Dementias (ADRD)'],
    'HSV-1 Infected (per 1,000 person-years)': [15.6, 12.3],
    'Non-Infected (per 1,000 person-years)': [9.8, 6.5],
    'CI Range Infected': ['(13.5–17.7)', '(10.8–13.8)'],  # Confidence Intervals for HSV-1 Infected
    'CI Range Non-Infected': ['(8.5–11.1)', '(5.5–7.5)']  # Confidence Intervals for Non-Infected
}

# Creating DataFrame
incidence_df = pd.DataFrame(incidence_data)

# Saving the table to a CSV file
incidence_df.to_csv('incidence_rate_analysis.csv', index=False)

# Displaying the table
print("\nIncidence Rate Analysis Table:")
print(incidence_df)

# Generating a bar chart for Incidence Rates
fig, ax = plt.subplots()
x_labels = incidence_df['Outcome']
y1_values = incidence_df['HSV-1 Infected (per 1,000 person-years)']
y2_values = incidence_df['Non-Infected (per 1,000 person-years)']

# Plotting the bars
bars1 = ax.bar(x_labels, y1_values, color='blue', label='HSV-1 Infected', alpha=0.7, width=0.4)
bars2 = ax.bar(x_labels, y2_values, color='orange', label='Non-Infected', alpha=0.7, width=0.4, align='edge')

# Adjusted annotations for HSV-1 Infected bars
for bar, ci in zip(bars1, incidence_data['CI Range Infected']):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1,  # Lowered y position slightly
            f"{bar.get_height()}\n{ci}", ha='center', va='bottom', fontsize=8)

# Adjusted annotations for Non-Infected bars
for bar, ci in zip(bars2, incidence_data['CI Range Non-Infected']):
    ax.text(bar.get_x() + bar.get_width() / 1.6, bar.get_height() + 0.1,  # Moved text slightly left
            f"{bar.get_height()}\n{ci}", ha='center', va='bottom', fontsize=8)

ax.set_ylabel('Incidence Rate per 1,000 person-years')
ax.set_title('Incidence Rate Comparison: HSV-1 Infected vs Non-Infected Cohorts')
ax.legend()
plt.tight_layout()

# Saving the bar chart as an image
plt.savefig('incidence_rate_bar_chart_fixed.png')
plt.show()

print("\nIncidence Rate Analysis Table and adjusted bar chart have been saved in your current working directory.")
