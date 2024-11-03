def prim(w,n,s):
    # Inicializar lista de vértices visitados con 0 (no visitado)
    v = []
    # Llenar la lista de vértices visitados con ceros hasta que tenga tamaño n
    while(len(v) != n):
        v.append(0)
    
    # Marcar el vértice de inicio s como visitado
    v[s] = 1
    # Inicializar la lista de aristas del árbol generador mínimo
    E = []
    suma = 0
    # Repetir el proceso n-1 veces para encontrar las aristas del MST
    
    for i in range(0, n-1):
        # Inicializar el peso mínimo como un valor alto, en este caso, 9
        minimo = 9
        # Variable para almacenar el vértice que se agregará al MST
        agregar_vertice = 0
        # Variable para almacenar la arista de peso mínimo encontrada en esta iteración
        e = []
        # Recorrer todos los vértices
        
        for j in range(0,n):
            # Si el vértice j está en el MST (es decir, v[j] == 1)
            if (v[j] == 1):
                # Recorrer los vecinos del vértice j
                
                for k in range(0, n):
                    # Si el vértice k no está en el MST y la arista j-k es la más pequeña encontrada
                    if(v[k] == 0 and w[j][k] < minimo):
                        # Actualizar el vértice a agregar
                        agregar_vertice = k 
                        # Actualizar la arista seleccionada
                        e = [j, k] 
                        print(f"Vertice seleccionado en la iteración: {[e[0] + 1, e[1] + 1]}")
                        # Actualizar el peso mínimo encontrado
                        minimo = w[j][k]
        
        # Agregar el peso de la arista seleccionada a la suma total
        suma += w[e[0]][e[1]]
        # Marcar el vértice recién agregado como visitado en la lista v
        v[agregar_vertice] = 1
        # Agregar la arista seleccionada a la lista de aristas del MST
        E.append([e[0] + 1, e[1] + 1])
    
    return [E,suma]

n = 6
s = 0
w = [#1,2,3,4,5,6  #9 == no existe la arista que conecte esos vertices
     [9,3,2,3,9,9],# conexion del nodo 1 con otros nodos
     [3,9,1,9,5,6],# conexion del nodo 2 con otros nodos
     [2,1,9,2,7,8],# conexion del nodo 3 con otros nodos
     [3,9,2,9,9,6],# conexion del nodo 4 con otros nodos
     [9,5,7,9,9,4],# conexion del nodo 5 con otros nodos
     [9,9,8,6,4,9] # conexion del nodo 6 con otros nodos
     ]

arbol_minimo_costo, costo = prim(w,n,s)
print(arbol_minimo_costo)
print(costo)
