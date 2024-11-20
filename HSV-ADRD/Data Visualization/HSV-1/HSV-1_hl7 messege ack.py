import matplotlib.pyplot as plt
import pandas as pd  # Import pandas

# Sample data for HL7 Message Acknowledgement
hl7_data = {
    'Message Type': ['Application Accept (AA)', 'Application Error (AE)', 'Application Reject (AR)', 'No Information (NI)'],
    'Percentage': [78.5, 19.5, 0.02, 1.17]
}

# Convert to DataFrame
df_hl7 = pd.DataFrame(hl7_data)

# Horizontal bar plot
plt.figure(figsize=(10, 6))
plt.barh(df_hl7['Message Type'], df_hl7['Percentage'], color='skyblue')
plt.title('Types of HL7 Message Acknowledgement')
plt.xlabel('Percentage (%)')
plt.show()
