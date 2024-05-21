import networkx as nx
import matplotlib.pyplot as plt

# Definimos las relaciones familiares en un diccionario
familia = {
    "Marcelo": {"hijos": ["Remedios", "Nestor", "Severino"]},
    "Cristina": {"hijos": ["Nestor", "Severino", "Remedios"]},
    "Santusa": {"hijos": ["Betty", "Agusto"]},
    "Nestor": {"hijos": ["yo", "Gerson", "Damaris"]},
    "Betty": {"hijos": ["yo", "Gerson", "Damaris"]},
    "Remedios": {"hijos": ["Abel", "Sandra"]},
    "Severino": {"hijos": []},
    "Agusto": {"hijos": ["Nami"]},
}

# Creamos un grafo dirigido
G = nx.DiGraph()

# Añadimos nodos y relaciones al grafo
for parent, relations in familia.items():
    for hijo in relations["hijos"]:
        G.add_edge(parent, hijo)

# Definimos las posiciones de los nodos en el grafo, aumentando el valor de k para mayor separación
pos = nx.spring_layout(G, k=2, iterations=50)

# Dibujamos el grafo
plt.figure(figsize=(12, 10))
nx.draw(G, pos, with_labels=True, node_size=2500, node_color='skyblue', font_size=10, font_weight='bold', arrows=True)
plt.title("Árbol Genealógico Familiar")
plt.show()
