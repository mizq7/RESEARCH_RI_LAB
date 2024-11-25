import pandas as pd
import os

# Create the data
data = [
    [26929004, 'SNOMED', "Alzheimer's disease", 23124, 24589, 5888, 6395, 'Condition'],
    [331, 'ICD9CM', "Alzheimer's disease", 15387, 15387, 0, 0, 'Condition'],
    ['G30.0', 'ICD10CM', "Alzheimer's disease with early onset", 311, 311, 0, 0, 'Condition'],
    ['G30.1', 'ICD10CM', "Alzheimer's disease with late onset", 1154, 1154, 0, 0, 'Condition'],
    ['G30.9', 'ICD10CM', "Alzheimer's disease, unspecified", 7525, 7525, 0, 0, 'Condition'],
    [52448006, 'SNOMED', 'Dementia', 30560, 110249, 11423, 41063, 'Condition'],
    [281004, 'SNOMED', 'Dementia associated with alcoholism', 487, 487, 237, 237, 'Condition'],
    [191519005, 'SNOMED', 'Dementia associated with another disease', 13994, 32754, 6709, 14940, 'Condition'],
    [1591000119102, 'SNOMED', 'Dementia with behavioral disturbance', 6012, 6637, 3261, 3673, 'Condition'],
    [80098002, 'SNOMED', 'Diffuse Lewy body disease', 1578, 2907, 581, 998, 'Condition'],
    [191493005, 'SNOMED', 'Drug-induced dementia', 21, 508, 19, 256, 'Condition'],
    [230270009, 'SNOMED', 'Frontotemporal dementia', 1216, 1216, 394, 394, 'Condition'],
    [51928006, 'SNOMED', 'General paresis - neurosyphilis', 38, 38, 27, 27, 'Condition'],
    [58756001, 'SNOMED', "Huntington's chorea", 919, 919, 187, 187, 'Condition'],
    [428051000, 'SNOMED', 'Mild dementia', 249, 249, 178, 178, 'Condition'],
    [430771000, 'SNOMED', 'Moderate dementia', 107, 107, 71, 71, 'Condition'],
    [56267009, 'SNOMED', 'Multi-infarct dementia', 0, 4901, 0, 1554, 'Condition'],
    [10349009, 'SNOMED', 'Multi-infarct dementia with delirium', 137, 137, 115, 115, 'Condition'],
    [25772007, 'SNOMED', 'Multi-infarct dementia with delusions', 1477, 1477, 304, 304, 'Condition'],
    [14070001, 'SNOMED', 'Multi-infarct dementia with depression', 1715, 1715, 341, 341, 'Condition'],
    [70936005, 'SNOMED', 'Multi-infarct dementia, uncomplicated', 1572, 1572, 794, 794, 'Condition'],
    [40425004, 'SNOMED', 'Postconcussion syndrome', 10285, 10285, 4781, 4781, 'Condition'],
    [12348006, 'SNOMED', 'Presenile dementia', 0, 631, 0, 343, 'Condition'],
    ['290.11', 'ICD9CM', 'Presenile dementia with delirium', 54, 54, 0, 0, 'Condition'],
    [191452002, 'SNOMED', 'Presenile dementia with delirium', 54, 54, 34, 34, 'Condition'],
    ['290.12', 'ICD9CM', 'Presenile dementia with delusional features', 58, 58, 0, 0, 'Condition'],
    [31081000119102, 'SNOMED', 'Presenile dementia with delusions', 58, 58, 27, 27, 'Condition'],
    [191455000, 'SNOMED', 'Presenile dementia with depression', 15, 15, 8, 8, 'Condition'],
    ['290.13', 'ICD9CM', 'Presenile dementia with depressive features', 15, 15, 0, 0, 'Condition'],
    ['290.1', 'ICD9CM', 'Presenile dementia, uncomplicated', 193, 193, 0, 0, 'Condition'],
    [416780008, 'SNOMED', 'Primary degenerative dementia of the Alzheimer type, presenile onset', 311, 311, 143, 143,
     'Condition'],
    [416975007, 'SNOMED', 'Primary degenerative dementia of the Alzheimer type, senile onset', 1154, 1154, 364, 364,
     'Condition'],
    [268612007, 'SNOMED', 'Senile and presenile organic psychotic conditions', 219, 219, 157, 157, 'Condition'],
    [15662003, 'SNOMED', 'Senile dementia', 0, 15314, 0, 4374, 'Condition'],
    [312991009, 'SNOMED', 'Senile dementia of the Lewy body type', 1329, 1329, 417, 417, 'Condition'],
    [191461002, 'SNOMED', 'Senile dementia with delirium', 577, 577, 299, 299, 'Condition'],
    [371024007, 'SNOMED', 'Senile dementia with delusion', 4393, 4393, 922, 922, 'Condition'],
    [191459006, 'SNOMED', 'Senile dementia with depression', 4655, 4655, 989, 989, 'Condition'],
    [191457008, 'SNOMED', 'Senile dementia with depressive or paranoid features', 0, 4655, 0, 989, 'Condition'],
    ['290', 'ICD9CM', 'Senile dementia, uncomplicated', 3206, 3206, 0, 0, 'Condition'],
    [428350000, 'SNOMED', 'Severe dementia', 301, 301, 195, 195, 'Condition'],
    [429998004, 'SNOMED', 'Vascular dementia', 10, 7988, 7, 3213, 'Condition'],
    [288631000119101, 'SNOMED', 'Vascular dementia with behavioral disturbance', 625, 625, 412, 412, 'Condition'],
    [1627601000119105, 'SNOMED', 'Vascular dementia without behavioral disturbance', 2452, 2452, 1240, 1240,
     'Condition'],
    [191451009, 'SNOMED', 'Uncomplicated presenile dementia', 193, 193, 131, 131, 'Condition'],
    [191449005, 'SNOMED', 'Uncomplicated senile dementia', 3206, 3206, 1383, 1383, 'Condition']
]

# Create DataFrame
df = pd.DataFrame(data, columns=['Code', 'Vocabulary', 'Concept Name', 'RC', 'DRC', 'PC', 'DPC', 'Domain'])


# Function to save the table
def save_table(df, filename, use_default_location=True):
    if use_default_location:
        directory = '/Users/mizq7/PycharmProjects/RESEARCH_RI_LAB/HSV-ADRD/Cohort Concept Sets Table Generation'
    else:
        directory = os.getcwd()  # Current working directory

    if not os.path.exists(directory):
        os.makedirs(directory)

    full_path = os.path.join(directory, filename)
    df.to_csv(full_path, index=False)
    print(f"Table saved as {full_path}")


# Save the table
save_table(df, 'dementia_table.csv', use_default_location=True)

# Print the table
print(df.to_string(index=False))

# Generate summary
unique_concepts = df['Concept Name'].nunique()
total_concepts = len(df)
unique_vocabularies = df['Vocabulary'].nunique()
vocabulary_names = df['Vocabulary'].unique().tolist()
unique_domains = df['Domain'].nunique()
total_pc_sum = df['PC'].sum()

print(f"\nTotal Concepts: {total_concepts}")
print(f"Unique Concept Names: {unique_concepts}")
print(f"Duplicated Concept Names: {total_concepts - unique_concepts}")
print(f"Unique Vocabularies: {unique_vocabularies}")
print(f"Vocabulary Names: {vocabulary_names}")
print(f"Unique Domains: {unique_domains} ({df['Domain'].iloc[0]})")
print(f"Total PC Sum: {total_pc_sum}")

print("\nRC (Record Count): total number of records")
print("DRC (Distinct Record Count): number of unique records")
print("PC (Patient Count): total number of patients")
print("DPC (Distinct Patient Count): number of unique patients")