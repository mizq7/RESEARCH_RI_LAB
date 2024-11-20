import matplotlib.pyplot as plt
import seaborn as sns

# Create a figure and axis with seaborn's style
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(6, 6))

# Add a title at the top of the graph
plt.suptitle('HSV-1 Cohorts', fontsize=18, fontweight='bold')

# Define the positions and size of the boxes for each cohort
rect_coords = [
    (0.1, 0.55, 0.35, 0.35),  # Cohort A (top-left)
    (0.55, 0.55, 0.35, 0.35),  # Cohort B (top-right)
    (0.1, 0.1, 0.35, 0.35),  # Cohort C (bottom-left)
    (0.55, 0.1, 0.35, 0.35)  # Cohort D (bottom-right)
]

# Colors for each cohort box
colors = ['#FFDDC1', '#C1FFD7', '#FFC1F3', '#C1E7FF']

# Cohort Labels
cohorts = ['A', 'B', 'C', 'D']

# Create the matrix structure with light colors and separate gaps between the boxes
for i, (x, y, w, h) in enumerate(rect_coords):
    # Draw rectangles
    rect = plt.Rectangle((x, y), w, h, facecolor=colors[i], edgecolor="black", linewidth=2)
    ax.add_patch(rect)

    # Add text inside the boxes
    ax.text(x + w / 2, y + h / 2 + 0.05, 'Cohort', fontsize=14, ha='center', va='center', fontweight='bold')
    ax.text(x + w / 2, y + h / 2 - 0.05, cohorts[i], fontsize=28, ha='center', va='center',
            fontweight='bold')  # Larger letters for A, B, C, D

# Add column headers: "With Exclusions" and "Without Exclusions"
plt.text(0.275, 0.95, 'With Exclusions', fontsize=16, fontweight='bold', ha='center', va='center')
plt.text(0.725, 0.95, 'Without Exclusions', fontsize=16, fontweight='bold', ha='center', va='center')

# Add row headers: "3-Yr Follow-up" and "Indefinite"
plt.text(0.03, 0.725, '3-Yr Follow-up', fontsize=16, fontweight='bold', ha='center', va='center', rotation=90)
plt.text(0.03, 0.275, 'Indefinite', fontsize=16, fontweight='bold', ha='center', va='center', rotation=90)

# Remove axes and add proper limits to the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Display the plot
plt.show()
