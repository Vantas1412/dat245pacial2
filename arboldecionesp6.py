import networkx as nx
import matplotlib.pyplot as plt

# Definimos las relaciones familiares en un diccionario
familia = {
    "Seleccion": ["Abaddon", "Alchemist", "Anti Mage", "Axe"],
    "Abaddon": ["Heraldo", "Guardian", "Cruzado", "Arconte", "Leyenda"],
    "Anti Mage": ["Heraldo", "Guardian", "Cruzado", "Arconte", "Leyenda"],
    "Alchemist": ["Heraldo", "Guardian", "Cruzado", "Arconte", "Leyenda"],
    "Axe": ["Heraldo", "Guardian", "Cruzado", "Arconte", "Leyenda"],
    "Heraldo": ["Pierde", "Gana"],
    "Guardian": ["Pierde", "Gana"],
    "Cruzado": ["Pierde", "Gana"],
    "Arconte": ["Pierde", "Gana"],
    "Leyenda": ["Pierde", "Gana"],
}

# Creamos un grafo dirigido
G = nx.DiGraph()

# Añadimos nodos y relaciones al grafo
for parent, children in familia.items():
    for child in children:
        G.add_edge(parent, child)

# Definimos una disposición personalizada para que se parezca a un árbol
pos = nx.shell_layout(G)

# Dibujamos el grafo
plt.figure(figsize=(12, 10))
nx.draw(G, pos, with_labels=True, node_size=2500, node_color='skyblue', font_size=10, font_weight='bold', arrows=True)
plt.title("Árbol de Decisiones")
plt.show()
