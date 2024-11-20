import matplotlib.pyplot as plt
import networkx as nx

# Entities and relationships
entities = ["DHSS", "Providers", "Clinics", "Facilities", "Users", "Patients", "Vaccinations", "HL7 System"]
relationships = [
    ("DHSS", "Providers"),
    ("Providers", "Clinics"),
    ("Clinics", "Facilities"),
    ("Clinics", "Users"),
    ("Users", "Patients"),
    ("Patients", "Vaccinations"),
    ("Facilities", "HL7 System"),
    ("Clinics", "HL7 System")
]

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(entities)
G.add_edges_from(relationships)

# Draw graph
plt.figure(figsize=(12, 8))
nx.draw(G, with_labels=True, node_size=2500, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray', arrowsize=15)
plt.title("Qualitative Analysis: IIS Data Relationships and Infrastructural Challenges")
plt.show()
