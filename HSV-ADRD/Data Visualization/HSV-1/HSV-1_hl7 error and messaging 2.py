import matplotlib.pyplot as plt
import pandas as pd

# Data for tables represented as lists of dictionaries
tables_data = {
    "HL7 Log Type": {"Type": ['Get', 'Send', 'Rerun', 'Error'], "Percentage": [49.08, 49.92, 0.08, 0.0]},
    "HL7 Submission and Response": {"Type": ['Submissions', 'Responses'], "Percentage": [99.08, 99.19]},
    "Message Acknowledgment": {"Type": ['Application Accept', 'Application Error', 'Application Reject', 'No Information'], "Percentage": [78.5, 19.5, 0.02, 1.17]},
    "Error Type": {"Type": ['Application Error', 'Table Value Not Found', 'Required Field Missing', 'Other'], "Percentage": [54.47, 23.86, 11.38, 10.29]},
    "Error Severity": {"Type": ['Informational', 'Warning', 'Error'], "Percentage": [15.23, 67.04, 12.27]}
}

# Plotting
fig, axes = plt.subplots(3, 2, figsize=(15, 15))
fig.suptitle("Overview of HL7 Messaging and Data Quality Metrics", fontsize=16)

# Loop to plot each table data as a separate bar chart
for idx, (title, data) in enumerate(tables_data.items()):
    row, col = divmod(idx, 2)
    ax = axes[row, col]
    df = pd.DataFrame(data)
    ax.barh(df['Type'], df['Percentage'], color='steelblue')
    ax.set_title(title)
    ax.set_xlabel('Percentage (%)')
    for i, v in enumerate(df['Percentage']):
        ax.text(v + 1, i, f"{v:.2f}%", va='center')

# Hide the last subplot if necessary
axes[2, 1].axis('off')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
