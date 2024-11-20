import pandas as pd
import matplotlib.pyplot as plt

# Sample data for each table represented in dictionary format
data_log_type = {'Type': ['Get', 'Send', 'Rerun', 'Error'], 'Percentage': [49.08, 49.92, 0.08, 0.0]}
data_submission_response = {'Type': ['Submissions', 'Responses'], 'Percentage': [99.08, 99.19]}
data_acknowledgment = {'Type': ['Application Accept', 'Application Error', 'Application Reject', 'No Information'], 'Percentage': [78.5, 19.5, 0.02, 1.17]}
data_error_type = {'Type': ['Application Error', 'Table Value Not Found', 'Required Field Missing', 'Data Type Error', 'Other'], 'Percentage': [54.47, 23.86, 11.38, 4.78, 5.51]}
data_error_severity = {'Type': ['Informational', 'Warning', 'Error'], 'Percentage': [15.23, 67.04, 12.27]}

# Convert dictionaries to DataFrames
df_log_type = pd.DataFrame(data_log_type)
df_submission_response = pd.DataFrame(data_submission_response)
df_acknowledgment = pd.DataFrame(data_acknowledgment)
df_error_type = pd.DataFrame(data_error_type)
df_error_severity = pd.DataFrame(data_error_severity)

# Set up the figure and axes for subplots
fig, axes = plt.subplots(3, 2, figsize=(14, 12))  # 3 rows, 2 columns layout


# Plot for HL7 Log Type (Table 3)
axes[0, 0].barh(df_log_type['Type'], df_log_type['Percentage'], color='skyblue')
axes[0, 0].set_title("HL7 Log Type Distribution")
axes[0, 0].set_xlabel("Percentage (%)")
for index, value in enumerate(df_log_type['Percentage']):
    axes[0, 0].text(value, index, f"{value:.2f}%", va='center')

# Plot for HL7 Submission and Response (Table 4)
axes[0, 1].barh(df_submission_response['Type'], df_submission_response['Percentage'], color='lightgreen')
axes[0, 1].set_title("HL7 Submission and Response Status")
axes[0, 1].set_xlabel("Percentage (%)")
for index, value in enumerate(df_submission_response['Percentage']):
    axes[0, 1].text(value, index, f"{value:.2f}%", va='center')

# Plot for HL7 Message Acknowledgment (Table 5)
axes[1, 0].barh(df_acknowledgment['Type'], df_acknowledgment['Percentage'], color='salmon')
axes[1, 0].set_title("HL7 Message Acknowledgment Types")
axes[1, 0].set_xlabel("Percentage (%)")
for index, value in enumerate(df_acknowledgment['Percentage']):
    axes[1, 0].text(value, index, f"{value:.2f}%", va='center')

# Plot for HL7 Error Type (Table 6)
axes[1, 1].barh(df_error_type['Type'], df_error_type['Percentage'], color='orange')
axes[1, 1].set_title("HL7 Error Type Distribution")
axes[1, 1].set_xlabel("Percentage (%)")
for index, value in enumerate(df_error_type['Percentage']):
    axes[1, 1].text(value, index, f"{value:.2f}%", va='center')

# Plot for HL7 Error Severity (Table 7)
axes[2, 0].barh(df_error_severity['Type'], df_error_severity['Percentage'], color='plum')
axes[2, 0].set_title("HL7 Error Severity Levels")
axes[2, 0].set_xlabel("Percentage (%)")
for index, value in enumerate(df_error_severity['Percentage']):
    axes[2, 0].text(value, index, f"{value:.2f}%", va='center')

# Hide the empty subplot
axes[2, 1].axis('off')

# Layout adjustments
plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to fit title
plt.show()
