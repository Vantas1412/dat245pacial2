# Definición del grafo como un diccionario de adyacencia
g = {
    'A': {'B': 2, 'C': 3, 'D': 1, 'E': 4, 'F': 2, 'G': 3, 'H': 5},
    'B': {'A': 2, 'C': 2, 'D': 2, 'E': 3, 'F': 1, 'G': 2, 'H': 4},
    'C': {'A': 3, 'B': 2, 'D': 2, 'E': 5, 'F': 3, 'G': 1, 'H': 2},
    'D': {'A': 1, 'B': 2, 'C': 2, 'E': 3, 'F': 2, 'G': 4, 'H': 1},
    'E': {'A': 4, 'B': 3, 'C': 5, 'D': 3, 'F': 2, 'G': 1, 'H': 2},
    'F': {'A': 2, 'B': 1, 'C': 3, 'D': 2, 'E': 2, 'G': 3, 'H': 1},
    'G': {'A': 3, 'B': 2, 'C': 1, 'D': 4, 'E': 1, 'F': 3, 'H': 2},
    'H': {'A': 5, 'B': 4, 'C': 2, 'D': 1, 'E': 2, 'F': 1, 'G': 2}
}

# Función para generar todas las posibles combinaciones de caminos
def gc(g, na, v, ca, tc):
    if len(v) == len(g):
        tc.append(ca[:])
        return

    for vn, p in g[na].items():
        if vn not in v:
            v.add(vn)
            ca.append(vn)
            gc(g, vn, v, ca, tc)
            v.remove(vn)
            ca.pop()

# Función principal para obtener todas las posibles combinaciones de caminos
def gtc(g):
    tc = []
    for ni in g.keys():
        v = set()
        v.add(ni)
        ca = [ni]
        gc(g, ni, v, ca, tc)
    return tc

# Obtener todas las posibles combinaciones de caminos
tc = gtc(g)
print("Todos los posibles caminos:")
print(len(tc))
