Laberinto con Backtracking v1.5

Autores:
- Enmanuel C. -- 1124404
- Dominique J. -- 1121623

Descripción

Este proyecto es un **juego de laberinto interactivo** desarrollado en
Python usando **Tkinter**. Permite al jugador recorrer un laberinto
generado aleatoriamente, con la posibilidad de moverse manualmente con
las flechas del teclado o dejar que un **solucionador automático con
backtracking** encuentre la salida paso a paso.

El juego incluye animaciones, colores para el rastro del jugador,
efectos de celebración al llegar a la meta y una interfaz gráfica con
botones para generar un nuevo laberinto, resolver automáticamente o
detener la resolución.

Funcionalidades

1.  Generación de laberintos aleatorios:
    -   Laberintos de cualquier tamaño impar mayor a 5x5.
    -   Caminos y paredes generados mediante backtracking recursivo.
    -   La salida siempre está ubicada en la esquina inferior derecha.

2.  Control del jugador:
    -   Movimiento manual usando las flechas del teclado.
    -   Rastro visual con colores cambiantes.
    -   Detección de llegada a la meta con animación de celebración.

3.  Solucionador automático:
    -   Resuelve el laberinto usando **backtracking iterativo**.
    -   Se puede iniciar desde la posición actual del jugador.
    -   Generador paso a paso para animación de la solución.
    -   Movimientos manuales detienen la resolución automática y
        permiten retomar más tarde.

4.  Interfaz gráfica:*
    -   Panel lateral con botones:
        -   Nuevo laberinto
        -   Resolver/Continuar
        -   Detener
    -   Canvas principal donde se dibuja el laberinto y los movimientos
        del jugador.
    -   Créditos de los autores en el panel lateral.


Estructura del proyecto

    ProyectoFinal_Laberinto/
    │
    ├─ core/
    │   ├─ maze_generator.py      # Genera laberatos aleatorios
    │   ├─ solver.py              # Solucionador automático con backtracking
    │   └─ player.py              # Clase Player y movimiento del jugador
    │
    ├─ ui/
    │   ├─ builder.py             # Construcción de la interfaz gráfica
    │   └─ colors.py              # Paleta de colores usada en el juego
    │
    ├─ main.py                    # Archivo principal que inicia el juego
    ├─ README.md                  # Documentación del proyecto
    └─ ...

Uso:

1.  Ejecuta `main.py` para iniciar el juego.
2.  Usa las flechas del teclado para mover al jugador manualmente.
3.  Botones del panel lateral:

    -   Nuevo laberinto: genera un laberinto aleatorio.
    -   Resolver/Continuar: activa el solucionador automático desde
        la posición actual.
    -   Detener: detiene la resolución automática en curso.

4.  Al llegar a la meta, se muestra una animación de celebración.

Cómo funciona el solucionador automático

-   Implementado como un generador iterativo que recorre el
    laberinto con backtracking.
-   Cada paso devuelve la siguiente celda que debe visitar el jugador.
-   Vecinos se exploran en orden aleatorio, pero la meta se prioriza al
    final para que el generador explore primero otras rutas.
-   Permite animación paso a paso sin bloquear la interfaz gráfica.

Créditos y agradecimientos

-   Autores: Enmanuel C. y Dominique J.\
-   Tecnologías: Python, Tkinter
-   Inspiración basada en algoritmos de generación y resolución de
    laberintos mediante backtracking.
