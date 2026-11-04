import random

def generate_maze(rows, cols):
    # Crea una matriz vacía llena de ceros (paredes)
    maze = [[0] * cols for _ in range(rows)]

    def backtrack(r, c):
    # Posibles movimientos: dos celdas a la derecha, izquierda, abajo o arriba
        dirs = [(0, 2), (0, -2), (2, 0), (-2, 0)]
    # Baraja los movimientos para que el laberinto sea diferente cada vez
        random.shuffle(dirs)
        
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            # Comprueba si la celda destino está dentro del laberinto y aún no ha sido visitada
            if (1 <= nr < rows - 1 and 1 <= nc < cols - 1 and maze[nr][nc] == 0):
                 # Marca como camino la celda intermedia entre la actual y la siguiente
                maze[r + dr // 2][c + dc // 2] = 1
                 # Marca como camino la nueva celda
                maze[nr][nc] = 1
                 # Llama recursivamente para continuar creando caminos desde la nueva celda
                backtrack(nr, nc)

    # Punto de inicio del laberinto
    maze[1][1] = 1
    backtrack(1, 1)
    # Punto de salida del laberinto
    maze[rows - 2][cols - 2] = 1
    # Devuelve la matriz del laberinto generado
    return maze
