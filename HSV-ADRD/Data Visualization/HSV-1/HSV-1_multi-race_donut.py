import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data representing the percentage of patients by the number of races identified
data = {
    'Number of Races Identified': [
        'No Race Assigned', 'Single Race', 'Two Races',
        'Three Races', 'Four Races', 'Five Races', 'Six Races'
    ],
    'Percentage of Patients': [18.83, 75.85, 3.64, 1.20, 0.44, 0.05, 0.01]
}

df = pd.DataFrame(data)

# Create a donut plot
plt.figure(figsize=(8, 8))
colors = sns.color_palette('pastel')[0:7]

# Create a pie chart
plt.pie(df['Percentage of Patients'], labels=df['Number of Races Identified'], colors=colors,
        autopct='%1.1f%%', startangle=140, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})

# Draw a circle at the center to turn the pie into a donut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Distribution of Patients by Number of Race Categories Identified')
plt.tight_layout()
plt.show()
