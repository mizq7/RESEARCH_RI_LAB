import pandas as pd

# Sample data as provided in the earlier steps
data = {
    "Medication Category": [
        "Valacyclovir", "Acyclovir", "Famciclovir", "Penciclovir", "Foscarnet",
        "Gabapentin", "Pregabalin", "Amitriptyline", "Donepezil", "Memantine",
        "Sertraline", "Citalopram", "Risperidone", "Quetiapine", "Valproic Acid", "Carbamazepin"
    ],
    "Cohort Count": [1946] * 16,
    "Person Count": [989, 449, 210, 12, 5, 74, 33, 30, 4, 2, 65, 13, 4, 14, 5, 5],
    "Utilization in Pathway Cohort (%)": [42.36, 19.23, 8.46, 0.51, 0.21, 3.17, 1.41, 1.28, 0.17, 0.09, 2.78, 0.56, 0.17, 0.60, 0.21, 0.21],
    "Pathway Percentage": [42.36, 19.23, 8.46, 0.51, 0.21, 3.17, 1.41, 1.28, 0.17, 0.09, 2.78, 0.56, 0.17, 0.60, 0.21, 0.21],
    "Cohort Percentage": [26.64, 12.10, 5.66, 0.32, 0.13, 1.99, 0.89, 0.81, 0.11, 0.05, 1.75, 0.35, 0.11, 0.38, 0.13, 0.13],
    "Indication": [
        "Primary HSV-1 Treatment", "Primary HSV-1 Treatment", "Primary HSV-1 Treatment",
        "Alternative HSV-1 Medication", "Alternative HSV-1 Medication",
        "Long-term Neuropathic Effects", "Long-term Neuropathic Effects", "Long-term Neuropathic Effects",
        "All Stages Dementia", "Moderate to Severe Dementia",
        "Antidepressants for Cognitive Decline", "Antidepressants for Cognitive Decline",
        "Antipsychotics for Cognitive Decline", "Antipsychotics for Cognitive Decline",
        "Mood Stabilizers", "Mood Stabilizers"
    ],
    "Combination Medication Use": [
        "", "", "", "", "", "Gabapentin + Donepezil: 1 patient (0.08%)",
        "Valacyclovir + Amitriptyline + Sertraline: 2 patients (0.16%)",
        "Pregabalin + Gabapentin + Memantine: 1 patient (0.08%)", "", "", "", "", "", "", "", ""
    ]
}

# Creating DataFrame
medication_table = pd.DataFrame(data)

# Saving as Excel
medication_table.to_excel("Medication_and_Combination_Use_Statistics.xlsx", index=False)
