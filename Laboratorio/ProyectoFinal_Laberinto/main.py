import tkinter as tk
from tkinter import messagebox
from core.game import MazeGame

root = tk.Tk()
root.withdraw()

respuesta = messagebox.askyesno("Pregunta", "¿Quieres que se haga solo?")
modo_auto = bool(respuesta)

root.deiconify()

if __name__ == "__main__":
    MazeGame(root, modo_auto=modo_auto)
    root.mainloop()
