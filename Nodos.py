import networkx as nx
import matplotlib.pyplot as plt

class Nodo:
    def __init__(self, estado, heuristica, hijos=None):
        self.estado = estado
        self.heuristica = heuristica
        self.hijos = hijos if hijos is not None else []

def escalada_simple(nodo):
    print(f"Visitando nodo: {nodo.estado} con heurística: {nodo.heuristica}")
    while nodo.hijos:
        hijo_min = min(nodo.hijos, key=lambda x: x.heuristica)
        if hijo_min.heuristica >= nodo.heuristica:
            break
        nodo = hijo_min
        print(f"Visitando nodo: {nodo.estado} con heurística: {nodo.heuristica}")
    return nodo

def escalada_maxima_pendiente(nodo):
    print(f"Visitando nodo: {nodo.estado} con heurística: {nodo.heuristica}")
    while nodo.hijos:
        hijo_min = min(nodo.hijos, key=lambda x: x.heuristica)
        if hijo_min.heuristica >= nodo.heuristica:
            break
        nodo = hijo_min
        print(f"Visitando nodo: {nodo.estado} con heurística: {nodo.heuristica}")
    return nodo

def construir_arbol(grafo, nodo, parent=None, nivel=0, pos=None, x=0, dx=1):
    if pos is None:
        pos = {}
    pos[nodo.estado] = (x, -nivel)
    if parent:
        grafo.add_edge(parent.estado, nodo.estado)
    hijos_n = len(nodo.hijos)
    for i, hijo in enumerate(nodo.hijos):
        construir_arbol(grafo, hijo, nodo, nivel+1, pos, x - dx/2 + i*dx/hijos_n, dx/hijos_n)
    return pos

def dibujar_arbol(grafo, pos):
    plt.figure(figsize=(12, 8))
    nx.draw(grafo, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", font_color="black", arrows=False)
    plt.show()

# Construcción del árbol
n = Nodo("N", 1, [Nodo("O", 0)])
l = Nodo("L", 4, [n])
m = Nodo("M", 3)
i = Nodo("I", 6, [l, m])
j = Nodo("J", 0)
k = Nodo("K", 5)
h = Nodo("H", 7, [j, k])
g = Nodo("G", 8)
d = Nodo("D", 8, [g, h, i])
e = Nodo("E", 8)
f = Nodo("F", 7)
b = Nodo("B", 9, [e, f])
c = Nodo("C", 9)
a = Nodo("A", 10, [b, c, d])

print("Escalada Simple:")
resultado_simple = escalada_simple(a)
print(f"Nodo final: {resultado_simple.estado} con heurística: {resultado_simple.heuristica}")

print("\nEscalada por Máxima Pendiente:")
resultado_maxima_pendiente = escalada_maxima_pendiente(a)
print(f"Nodo final: {resultado_maxima_pendiente.estado} con heurística: {resultado_maxima_pendiente.heuristica}")

# Construcción y dibujo del árbol de búsqueda
grafo = nx.DiGraph()
pos = construir_arbol(grafo, a)
dibujar_arbol(grafo, pos)
