import plotly.graph_objects as go

# Sample data
labels = [
    "Main Medication", "Alternative Medication", "Long Effect Medication",
    "Memory Dysfunction/ADRD", "Valacyclovir", "Acyclovir", "Famciclovir",
    "Gabapentin", "Sertraline", "Donepezil", "Rivastigmine", "Memantine"
]
parents = [
    "", "Main Medication", "Main Medication", "Main Medication",
    "Memory Dysfunction/ADRD", "Memory Dysfunction/ADRD", "Memory Dysfunction/ADRD",
    "Memory Dysfunction/ADRD", "Memory Dysfunction/ADRD", "Memory Dysfunction/ADRD",
    "Memory Dysfunction/ADRD", "Memory Dysfunction/ADRD"
]
values = [1332, 640, 414, 272, 215, 136, 127, 100, 82, 76, 72, 59]

# Create sunburst plot
fig = go.Figure(go.Sunburst(
    labels=labels,
    parents=parents,
    values=values,
    branchvalues="total"
))

fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

fig.show()
