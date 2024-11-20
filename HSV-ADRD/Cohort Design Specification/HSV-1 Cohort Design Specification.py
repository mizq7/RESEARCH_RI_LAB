import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


def create_box(ax, x, y, max_width, title, content, color):
    wrapped_text = wrap_text(content, int(max_width * 200))
    text = ax.text(x, y, wrapped_text, ha='center', va='center', wrap=True, fontsize=6)

    bbox = text.get_window_extent(renderer=ax.figure.canvas.get_renderer())
    bbox_data = bbox.transformed(ax.transData.inverted())
    padding = 0.001
    new_width = min(max_width, bbox_data.width + padding)
    new_height = bbox_data.height + padding

    rect = patches.Rectangle((x - new_width / 2, y - new_height / 2), new_width, new_height, fill=True, facecolor=color,
                             edgecolor='black', linewidth=0.5, alpha=0.3)
    ax.add_patch(rect)

    ax.text(x, y + new_height / 2 + 0.001, title, ha='center', va='bottom', fontweight='bold', fontsize=7)

    return new_width, new_height, y - new_height / 2, y + new_height / 2, x - new_width / 2, x + new_width / 2


def wrap_text(text, max_width):
    words = text.split()
    lines = []
    current_line = []
    current_width = 0
    for word in words:
        word_width = len(word)
        if current_width + word_width <= max_width:
            current_line.append(word)
            current_width += word_width + 1
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_width = word_width
    lines.append(' '.join(current_line))
    return '\n'.join(lines)


def add_arrow(ax, start, end, style):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', linestyle='solid' if style == 'solid' else 'dashed',
                                color='black', linewidth=0.5, shrinkA=0, shrinkB=0))


def create_cohort(ax, x, y, width, height, color, cohort_letter):
    if cohort_letter in ['A', 'B']:
        ax.text(x + width / 2, y + height + 0.005, f"Cohort {cohort_letter}", ha='center', va='bottom',
                fontweight='bold', fontsize=10)
        ax.axhline(y=y + height - 0.002, xmin=x / 1.02, xmax=(x + width) / 1.02, color='black', linewidth=0.5)
    else:
        ax.text(x + width / 2, y - 0.005, f"Cohort {cohort_letter}", ha='center', va='top', fontweight='bold',
                fontsize=10)
        ax.axhline(y=y + 0.002, xmin=x / 1.02, xmax=(x + width) / 1.02, color='black', linewidth=0.5)

    # First layer
    w1, h1, y1_bottom, y1_top, x1_left, x1_right = create_box(ax, x + width / 2, y + height * 0.9, width,
                                                              "Condition Occurrence",
                                                              "Patients infected with\nHSV-1 for the first time", color)

    # Second layer
    inclusion_text = ("≥ 1 condition occurrence between 365 days prior to index and 1095 days post-index"
                      if cohort_letter in ['A', 'B'] else
                      "≥ 1 condition occurrence between 365 days prior to index and indefinite days post-index")
    exclusion_text = (
        "≤ 0 condition occurrence of any excluded diseases between all time prior to index and all time post-index"
        if cohort_letter in ['A', 'C'] else
        "Exclusion criteria not implemented")
    observation_text = "Event will persist until the end of continuous observation for the condition exposure"

    y2 = y + height * 0.55
    w2_left, h2_left, y2_left_bottom, y2_left_top, x2_left_left, x2_left_right = create_box(ax, x + width * 0.16, y2,
                                                                                            width * 0.32,
                                                                                            "Inclusion Criteria",
                                                                                            inclusion_text, color)
    w2_mid, h2_mid, y2_mid_bottom, y2_mid_top, x2_mid_left, x2_mid_right = create_box(ax, x + width * 0.5, y2,
                                                                                      width * 0.32,
                                                                                      "Exclusion Criteria",
                                                                                      exclusion_text, color)
    w2_right, h2_right, y2_right_bottom, y2_right_top, x2_right_left, x2_right_right = create_box(ax, x + width * 0.84,
                                                                                                  y2, width * 0.32,
                                                                                                  "Observation Period",
                                                                                                  observation_text,
                                                                                                  color)

    # Third layer
    med_exposure_text = "0 days of medication exposure prior to index date"
    med_observation_text = "Medication exposure event will persist until the end of continuous observation"

    y3 = y + height * 0.2
    w3_left, h3_left, y3_left_bottom, y3_left_top, x3_left_left, x3_left_right = create_box(ax, x + width * 0.245, y3,
                                                                                            width * 0.49,
                                                                                            "Medication Exposure Condition",
                                                                                            med_exposure_text, color)
    w3_right, h3_right, y3_right_bottom, y3_right_top, x3_right_left, x3_right_right = create_box(ax, x + width * 0.755,
                                                                                                  y3, width * 0.49,
                                                                                                  "Observation Period",
                                                                                                  med_observation_text,
                                                                                                  color)

    # Arrows
    add_arrow(ax, (x + width / 2, y1_bottom), (x + width * 0.16, y2_left_top), 'solid')
    add_arrow(ax, (x + width / 2, y1_bottom), (x + width * 0.5, y2_mid_top), 'solid')
    add_arrow(ax, (x + width / 2, y1_bottom), (x + width * 0.84, y2_right_top), 'solid')
    add_arrow(ax, (x + width * 0.16, y2_left_bottom), (x + width * 0.245, y3_left_top), 'dashed')
    add_arrow(ax, (x + width * 0.84, y2_right_bottom), (x + width * 0.755, y3_right_top), 'dashed')


def main():
    fig, ax = plt.subplots(figsize=(16, 16))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.title("HSV-1 Cohort Design", fontsize=20, fontweight='bold', y=1.02)

    colors = ['#FFDDC1', '#C1FFD7', '#FFC1F3', '#C1E7FF']
    cohorts = ['A', 'B', 'C', 'D']
    positions = [(0.01, 0.51), (0.51, 0.51), (0.01, 0.01), (0.51, 0.01)]

    for color, cohort, pos in zip(colors, cohorts, positions):
        create_cohort(ax, pos[0], pos[1], 0.48, 0.48, color, cohort)

    # Add plus sign separator
    ax.axhline(y=0.5, color='gray', linestyle='-', linewidth=1)
    ax.axvline(x=0.5, color='gray', linestyle='-', linewidth=1)

    plt.tight_layout()
    plt.savefig('HSV-1_Cohort_Design_Updated.png', dpi=300, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()