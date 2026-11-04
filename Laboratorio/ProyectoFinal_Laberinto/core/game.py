import sys
from ui.builder import build_ui
from core.maze_generator import generate_maze
from core.solver import solve_generator
from core.player import Player


class MazeGame:
    """Juego de laberinto con backtracking y control por flechas."""

    def __init__(self, master, rows=31, cols=31, cell_size=25, modo_auto=False):
        # Guardamos la ventana principal y configuraciones básicas del laberinto
        self.root = master
        self.rows = rows
        self.cols = cols
        self.cell = cell_size
        self.modo_auto = modo_auto
        self.solver_delay = 60

        # Validaciones: filas y columnas impares, tamaño mínimo 5x5
        if self.rows % 2 == 0 or self.cols % 2 == 0:
            raise ValueError("Las filas y columnas deben ser impares.")
        if self.rows < 5 or self.cols < 5:
            raise ValueError("El laberinto debe tener mínimo 5x5.")

        # Aumenta el límite de recursión para permitir laberintos grandes
        sys.setrecursionlimit(max(1000, self.rows * self.cols))

        # Inicializa la matriz del laberinto y estados del juego
        self.maze = [[0] * self.cols for _ in range(self.rows)]
        self.game_active = True
        self.solving = False
        self.solver_gen = None

        # Construye la interfaz gráfica y el jugador
        build_ui(self)  
        self.player = Player(self)

        # Genera un laberinto inicial
        self.new_maze()


        # Si el modo automático está activo, empieza a resolverlo solo
        if self.modo_auto:
            self.start_solving()


        # Vincula las teclas de flechas para mover al jugador
        self.root.bind("<Key>", self.on_key)

    def new_maze(self):
         # Detiene cualquier resolución automática en curso
        self.stop_solving()
        self.solver_gen = None
         # Genera un nuevo laberinto
        self.maze = generate_maze(self.rows, self.cols)
         # Dibuja el laberinto y coloca al jugador al inicio
        self.player.draw_maze()
        self.player.place_player()
         # Marca que el juego está activo
        self.game_active = True

    def start_solving(self):
       # Siempre recrea el generador del solucionador para que comience desde
       # la posición actual del jugador. Pasa el inicio explícitamente para que
       # el solucionador no vuelva a un estado anterior.
        self.solver_gen = solve_generator(self, start=tuple(self.player.pos))
         # Si no estaba resolviendo antes, inicia la animación del solucionador
        if not self.solving:
            self.solving = True
            self.step_solver()

    def stop_solving(self):
         # Simplemente detiene la resolución automática
        self.solving = False

    def step_solver(self):
           # Hace un paso del solucionador automático
        if not self.solving or not self.solver_gen:
            return
        try:
            # Obtiene la siguiente celda del solucionador
            nr, nc = next(self.solver_gen)
            cr, cc = self.player.pos
            dx = nc - cc
            dy = nr - cr
           # Indica que este movimiento es realizado por el solucionador,
           # para que no se detenga a sí mismo.
            self.player.move(dx, dy, by_solver=True)
           # Programa el siguiente paso después del retraso definido
            if self.solving and self.game_active:
                self.root.after(self.solver_delay, self.step_solver)
        except StopIteration:
           # Si el solucionador termina, detiene la animación
            self.solving = False
            self.solver_gen = None

    def on_key(self, event):
        # Diccionario que traduce las flechas a movimientos (dx, dy)
        moves = {"Up": (0, -1), "Down": (0, 1), "Left": (-1, 0), "Right": (1, 0)}
        # Si la tecla presionada es una flecha, mueve al jugador
        if event.keysym in moves:
            dx, dy = moves[event.keysym]
            self.player.move(dx, dy)
