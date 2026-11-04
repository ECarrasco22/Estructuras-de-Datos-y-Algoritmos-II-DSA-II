# import random

# def celebrate_win(game):
#     canvas = game.canvas
#     rows, cols, cell = game.rows, game.cols, game.cell

#  # Parpadeo en la meta con colores dorado y rojo
#     for i in range(6):
#         color = "gold" if i % 2 == 0 else "red"
#         x1 = (cols - 2) * cell
#         y1 = (rows - 2) * cell
#         x2, y2 = x1 + cell, y1 + cell
#         canvas.create_oval(x1 + 4, y1 + 4, x2 - 4, y2 - 4, fill=color, outline="black")
#         game.root.update()   # Actualiza la ventana para ver el cambio
#         game.root.after(150) # Espera un momento antes del siguiente parpadeo

#  # Efecto de círculos concéntricos alrededor del jugador
#     r, c = game.player.pos
#     cx = c * cell + cell // 2
#     cy = r * cell + cell // 2
#     for radius in range(10, 40, 5):
#         canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, fill="yellow", outline="")
#         game.root.update()
#         game.root.after(80)

#     # Texto central de celebración
#     text = canvas.create_text(cols * cell // 2, rows * cell // 2,
#                               text="¡META ALCANZADA! 🎉",
#                               font=("Arial", 36, "bold"), fill="lime")
#     game.root.update()

#  # Confeti aleatorio por toda la ventana
#     for _ in range(80):
#         cx = random.randint(0, cols * cell)
#         cy = random.randint(0, rows * cell)
#         canvas.create_oval(cx, cy, cx + 5, cy + 5,
#                            fill=random.choice(["red", "blue", "yellow", "pink", "green"]),
#                            outline="")
#         game.root.update()
#         game.root.after(15)

# # Borra el texto de celebración después de 2 segundos
#     game.root.after(2000, lambda: canvas.delete(text))
