from grafos2023 import GrafoLista

# Crear un objeto GrafoLista
g = GrafoLista()

g.adicionarVertice('A')
g.adicionarVertice('B')
g.adicionarVertice('C')
g.adicionarVertice('D')
g.adicionarVertice('E')
g.adicionarArco('A','B')
g.adicionarArco('B', 'E')
g.adicionarArco('B', 'C')
g.adicionarArco('C', 'D')
g.adicionarArco('D', 'A')
g.adicionarArco('E', 'D')

print(g)
# Contamos los ciclos simples del grafo
ciclos = g.contarCiclosSimples()

# Imprimimos el resultado
print("El grafo tiene", ciclos, "ciclos simples.")