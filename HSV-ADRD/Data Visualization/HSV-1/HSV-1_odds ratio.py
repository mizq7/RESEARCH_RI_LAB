import pandas as pd

# Sample data for Odds Ratio Analysis
odds_ratio_data = {
    'Outcome': ['Mild Cognitive Impairment (MCI)', 'Alzheimer’s Disease and Related Dementias (ADRD)'],
    'Odds Ratio (95% CI)': ['1.72 (1.58–1.87)', '2.03 (1.85–2.22)'],
    'p-value': ['<0.001', '<0.001']
}

# Creating DataFrame
odds_ratio_df = pd.DataFrame(odds_ratio_data)

# Saving the table to a CSV file
odds_ratio_df.to_csv('odds_ratio_analysis.csv', index=False)

# Displaying the table
print("\nOdds Ratio Analysis Table:")
print(odds_ratio_df)

print("\nOdds Ratio Analysis Table has been saved as 'odds_ratio_analysis.csv'.")
