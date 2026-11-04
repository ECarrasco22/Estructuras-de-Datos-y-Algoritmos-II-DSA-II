import tkinter as tk
from ui.colors import COLORS


def build_ui(game):
    # Configura la ventana principal
    game.root.title("Laberinto con Backtracking v1.5")
    game.root.configure(bg=COLORS["bg"])
    game.root.resizable(False, False)  # Ventana fija, no se puede redimensionar

    # Panel lateral derecho
    side = tk.Frame(game.root, bg=COLORS["bg"])
    side.pack(side="right", fill="y") # Ocupa toda la altura

    # Etiqueta con créditos de los autores
    tk.Label(
        side,
        text="Made By \nEnmanuel C.\n1124404\nDominique J.\n1121623",
        fg=COLORS["title"], bg=COLORS["bg"],
        font=("Arial Black", 12)
    ).pack(padx=10, pady=(20, 10))

    # Botón para generar un nuevo laberinto
    tk.Button(
        side, text="Nuevo laberinto",
        command=game.new_maze,
        bg=COLORS["btn_bg"], fg="white",
        activebackground=COLORS["btn_active"],
        font=("Arial", 12, "bold")
    ).pack(padx=10, pady=20)

    # Botón para resolver automáticamente o continuar la resolución
    tk.Button(
        side, text="Resolver/Continuar",
        command=game.start_solving,
        bg=COLORS["btn_Resolver_bg"], fg="white",
        activebackground=COLORS["btn_active"],
        font=("Arial", 12, "bold")
    ).pack(padx=25, pady=25)

   # Botón para detener la resolución automática
    tk.Button(
        side, text="Detener",
        command=game.stop_solving,
        bg=COLORS["btn_Detener_bg"], fg="white",
        activebackground=COLORS["btn_active"],
        font=("Arial", 12, "bold")
    ).pack(padx=30, pady=30)


    # Lienzo donde se dibuja el laberinto
    game.canvas = tk.Canvas(
        game.root,
        width=game.cols * game.cell,
        height=game.rows * game.cell,
        bg=COLORS["path"],
        highlightthickness=0
    )
    game.canvas.pack(side="left", fill="both", expand=True) # Llenar el espacio restante

    # Ajusta la ventana al tamaño requerido por el lienzo y el panel lateral
    game.root.update_idletasks()
    required_width = game.canvas.winfo_reqwidth() + side.winfo_reqwidth()
    required_height = max(game.canvas.winfo_reqheight(), side.winfo_reqheight())
    game.root.minsize(required_width, required_height)
    game.root.maxsize(required_width, required_height)
    game.root.geometry(f"{required_width}x{required_height}")  # Establece tamaño inicial
