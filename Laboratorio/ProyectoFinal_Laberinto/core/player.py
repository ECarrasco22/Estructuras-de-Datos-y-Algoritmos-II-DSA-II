import random
from tkinter import messagebox
from ui.colors import COLORS

class Player:
    def __init__(self, game):
            # Referencias al juego y al lienzo donde se dibuja
        self.game = game
        self.canvas = game.canvas
        self.cell = game.cell
        self.pos = [1, 1]

        
        # Colores posibles para el rastro del jugador
        self.trail_colors = ["#40B186", "#B3A318", "#C57122",
                             "#A72424", "#38810D", "#136868"]
        self.current_trail_color = random.choice(self.trail_colors)
        self.trail_positions = []
        ##

    def draw_maze(self):
        # Borra cualquier dibujo anterior del laberinto
        self.canvas.delete("maze")

        # Dibuja el fondo como camino abierto
        self.canvas.create_rectangle(0, 0, self.game.cols * self.cell,
                                     self.game.rows * self.cell,
                                     fill=COLORS["path"], outline="", tags="maze")
        # Dibuja las paredes del laberinto
        for r in range(self.game.rows):
            for c in range(self.game.cols):
                if self.game.maze[r][c] == 0:
                    x1, y1 = c * self.cell, r * self.cell
                    x2, y2 = x1 + self.cell, y1 + self.cell
                    self.canvas.create_rectangle(x1, y1, x2, y2,
                                                 fill=COLORS["wall"],
                                                 outline=COLORS["wall_outline"],
                                                 tags="maze")
        # Dibuja la meta (salida del laberinto)
        x1 = (self.game.cols - 2) * self.cell
        y1 = (self.game.rows - 2) * self.cell
        x2, y2 = x1 + self.cell, y1 + self.cell
        self.canvas.create_oval(x1 + 4, y1 + 4, x2 - 4, y2 - 4,
                                fill=COLORS["goal"], outline="black",
                                width=2, tags="maze")

    def place_player(self):
        # Posiciona al jugador en la celda inicial
        x1, y1 = 1 * self.cell + 5, 1 * self.cell + 5
        x2, y2 = x1 + self.cell - 10, y1 + self.cell - 10
        if hasattr(self, "player"):
            self.canvas.delete(self.player)
        self.player = self.canvas.create_oval(x1, y1, x2, y2,
                                              fill=COLORS["player"],
                                              outline=COLORS["player_outline"],
                                              width=2)
        # Reinicia posición y rastro del jugador
        self.pos = [1, 1]
        self.trail_positions = []
        self.current_trail_color = random.choice(self.trail_colors)

    def move(self, dx, dy, by_solver=False):
      # by_solver=True cuando el solucionador automático mueve al jugador.
      # Los movimientos manuales (by_solver=False) detendrán cualquier solucionador en ejecución
      # para que el usuario pueda tomar el control.
        if not self.game.game_active:
            return  # No mover si el juego terminó
        r, c = self.pos
        nr, nc = r + dy, c + dx
        # Verifica que la nueva posición esté dentro del laberinto y sea un camino
        if (0 <= nr < self.game.rows and 0 <= nc < self.game.cols and
                self.game.maze[nr][nc] == 1):
            # Si este es un movimiento manual y el solucionador está en ejecución,
            # se detiene y se descarta el generador actual,
            # para que se cree uno nuevo desde la posición actual
            # cuando el usuario solicite resolver nuevamente.

            # Detener el solucionador si el jugador se mueve manualmente
            if not by_solver and getattr(self.game, "solving", False):
                self.game.stop_solving()
                self.game.solver_gen = None

            # Cambia el color del rastro si se regresa a una celda ya visitada
            if [nr, nc] in self.trail_positions:
                self.current_trail_color = random.choice(self.trail_colors)
                self.trail_positions = []
            # Dibuja el rastro del jugador en la celda actual
            x1, y1 = c * self.cell + 6, r * self.cell + 6
            x2, y2 = x1 + self.cell - 12, y1 + self.cell - 12
            self.canvas.create_rectangle(x1, y1, x2, y2,
                                         fill=self.current_trail_color,
                                         outline="", tags="trail")
            self.trail_positions.append([r, c])

            # Actualiza la posición del jugador y mueve el dibujo en el lienzo
            self.pos = [nr, nc]
            self.canvas.move(self.player, dx * self.cell, dy * self.cell)

            # Comprueba si se llegó a la meta
            if nr == self.game.rows - 2 and nc == self.game.cols - 2:
                self.game.game_active = False
                messagebox.showinfo("¡Victoria!", "¡Has llegado a la salida!")
                self.game.solving = False
                self.game.solver_gen = None
