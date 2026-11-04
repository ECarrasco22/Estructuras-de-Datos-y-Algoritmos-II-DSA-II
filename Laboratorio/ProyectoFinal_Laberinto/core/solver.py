import random


def solve_generator(game, start=None):
    # Permite un inicio explícito para que el solucionador siempre comience
    # desde la posición actual del jugador cuando sea solicitado.

    # Permite definir un inicio explícito; por defecto usa la posición actual del jugador
    if start is None:
        start = tuple(game.player.pos)
    else:
        start = tuple(start)

    # Definimos la meta (la salida del laberinto)
    goal = (game.rows - 2, game.cols - 2)

    # Conjunto de celdas ya visitadas para evitar ciclos
    visited = {start}

    # Pila para backtracking: cada elemento tiene la celda actual y un iterador sobre sus vecinos
    stack = [(start, iter(neighbors(game, *start)))]

    while stack:
        (r, c), nbrs = stack[-1]
        
        # Si llegamos a la meta, terminamos
        if (r, c) == goal:
            break
        try:
            # Intentamos tomar el siguiente vecino
            nr, nc = next(nbrs)
        except StopIteration:
            # Si no hay más vecinos, retrocedemos (backtracking)
            stack.pop()
            if stack:
            # Devuelve la celda a la que retrocedemos
                yield stack[-1][0]
            continue

        # Si el vecino es válido y no ha sido visitado
        if (nr, nc) not in visited and game.maze[nr][nc] == 1:
            visited.add((nr, nc))
            yield (nr, nc)   # Devuelve esta celda como siguiente paso
            if (nr, nc) == goal:
                break

        # Agrega el vecino a la pila para continuar la búsqueda desde allí
            stack.append(((nr, nc), iter(neighbors(game, nr, nc))))


def neighbors(game, r, c):
   # Construir la lista de vecinos, barajarla para explorar en un orden no determinista
    nbrs = []
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:    # derecha, abajo, izquierda, arriba
        nr, nc = r + dr, c + dc
        if 0 <= nr < game.rows and 0 <= nc < game.cols and game.maze[nr][nc] == 1:
            nbrs.append((nr, nc))

   # Dar menor prioridad al objetivo para que el solucionador explore otras ramas primero.
   # Barajar solo los vecinos que no son el objetivo y agregar el objetivo al final
   # si está presente. Esto garantiza que el objetivo no será elegido
   # de inmediato, sin importar la disposición aleatoria del laberinto.

   # Dar menor prioridad a la meta para explorar otras ramas primero
    goal = (game.rows - 2, game.cols - 2)
    has_goal = goal in nbrs
    if has_goal:
        nbrs.remove(goal)


  # Barajamos los vecinos que no son meta para mayor aleatoriedad
    random.shuffle(nbrs)


  # Devolvemos primero los vecinos barajados
    for n in nbrs:
        yield n

 # Finalmente, si la meta estaba presente, la devolvemos al final
    if has_goal:
        yield goal
