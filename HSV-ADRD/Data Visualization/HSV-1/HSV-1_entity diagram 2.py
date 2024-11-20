import matplotlib.pyplot as plt
import networkx as nx

# Define the entities and their relationships
entities = [
    "DHSS", "Clinic", "Facility", "User",
    "Patient", "Vaccination", "Inventory", "HL7 Log"
]

# Define relationships as pairs of entities
relationships = [
    ("DHSS", "Clinic"),
    ("DHSS", "Facility"),
    ("Clinic", "User"),
    ("Clinic", "Patient"),
    ("Clinic", "Vaccination"),
    ("Patient", "Vaccination"),
    ("Vaccination", "Inventory"),
    ("Clinic", "HL7 Log"),
    ("Facility", "HL7 Log")
]

# Create a directed graph
G = nx.DiGraph()

# Add entities as nodes
G.add_nodes_from(entities)

# Add relationships as edges
G.add_edges_from(relationships)

# Draw the graph
plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold', edge_color='gray', arrowsize=20)
plt.title("IIS Data Model Entity Relationship Diagram", fontsize=14)
plt.show()
