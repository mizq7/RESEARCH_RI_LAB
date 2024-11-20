import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create figure and axis with more space between boxes and adjusted labels
fig, ax = plt.subplots(figsize=(6, 6))

# Title of the figure
plt.suptitle('HSV-1 Cohorts', fontsize=16, fontweight='bold')

# Adjusted coordinates for the rectangles to create more space between boxes
rect_coords = [
    (0.1, 0.55, 0.3, 0.3),  # Cohort A (top-left), adjusted smaller and with gaps
    (0.6, 0.55, 0.3, 0.3),  # Cohort B (top-right)
    (0.1, 0.15, 0.3, 0.3),  # Cohort C (bottom-left)
    (0.6, 0.15, 0.3, 0.3)  # Cohort D (bottom-right)
]

# Light color codes for the cohorts
colors = ['#FFDDC1', '#C1FFD7', '#FFC1F3', '#C1E7FF']

# Cohort Labels
cohorts = ['A', 'B', 'C', 'D']

# Draw the rectangles and text inside them
for i, (x, y, w, h) in enumerate(rect_coords):
    # Draw the rectangle with light colors
    ax.add_patch(patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05", edgecolor="black", facecolor=colors[i],
                                        linewidth=2))

    # Add the cohort label in two lines
    ax.text(x + w / 2, y + h / 2 + 0.05, 'Cohort', fontsize=16, ha='center', va='center', fontweight='bold')
    ax.text(x + w / 2, y + h / 2 - 0.05, cohorts[i], fontsize=32, ha='center', va='center',
            fontweight='bold')  # Larger letters A, B, C, D

# Add the headers above the boxes, adjusted closer to the boxes
plt.text(0.275, 0.95, 'With Exclusions', fontsize=16, fontweight='bold', ha='center', va='center')
plt.text(0.775, 0.95, 'Without Exclusions', fontsize=16, fontweight='bold', ha='center', va='center')

# Adjusted the row headers: moved them slightly up and shifted "Indefinite" to the left
plt.text(0.02, 0.72, '3-Yr Follow-up', fontsize=16, fontweight='bold', ha='center', va='center', rotation=90)
plt.text(0.02, 0.32, 'Indefinite', fontsize=16, fontweight='bold', ha='center', va='center', rotation=90)

# Remove axes and adjust limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.1)
ax.axis('off')  # Hide the axis

# Display the plot
plt.show()
