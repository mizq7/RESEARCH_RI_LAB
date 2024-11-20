import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data Preparation
data = {
    'Provider': {
        'Value-Set Codes': ['ACTIVE_STATUS', 'STATE', 'ZIP_CODE'],
        'Invalid %': [0.00, 1.49, 1.53]
    },
    'Clinic': {
        'Value-Set Codes': ['ACTIVE_STATUS', 'STATE', 'ZIP_CODE'],
        'Invalid %': [0.00, 0.05, 0.05]
    },
    'Patient': {
        'Value-Set Codes': ['GENDER', 'RACES', 'ETHNICITY'],
        'Invalid %': [0.01, 18.82, 19.11]
    },
    'Patient Vaccination': {
        'Value-Set Codes': ['VACCINATION_CODE_ID', 'VFC_CODE_ID'],
        'Invalid %': [0.00, 4.08]
    },
    'Inventory': {
        'Value-Set Codes': ['VACCINATION_CODE_ID', 'NDC_NUMBER', 'FUNDING_SOURCE_ACTIVE_STATUS'],
        'Invalid %': [0.00, 0.01, 0.00]
    }
}


# Function to create a donut plot for an entity
def create_donut_plot(entity_name, entity_data):
    labels = entity_data['Value-Set Codes']
    sizes = entity_data['Invalid %']

    # Calculate the percentage of valid data
    valid_percentages = [100 - x for x in sizes]

    # For donut plot, we need to have two sets of data: invalid and valid
    data_for_plot = []
    labels_for_plot = []
    for i in range(len(labels)):
        data_for_plot.extend([sizes[i], valid_percentages[i]])
        labels_for_plot.extend([f"{labels[i]} Invalid", f"{labels[i]} Valid"])

    # Colors for the plot
    colors = sns.color_palette('pastel', len(data_for_plot))

    # Create the donut plot
    plt.figure(figsize=(8, 8))
    plt.pie(data_for_plot, labels=labels_for_plot, colors=colors,
            autopct='%1.1f%%', startangle=90, pctdistance=0.85, textprops={'fontsize': 10})

    # Draw circle in the center to make it a donut plot
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    plt.title(f"{entity_name} - Value-Set Compliance", fontsize=14)
    plt.tight_layout()
    plt.show()


# Create donut plots for each entity
for entity_name, entity_data in data.items():
    create_donut_plot(entity_name, entity_data)
