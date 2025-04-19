# Ejercicio 1: Módulos y constantes globales

"""
Enunciado:
1. Crea un archivo `settings.py` que defina tres constantes:
   - WIDTH: ancho de la ventana (por ejemplo 650)
   - HEIGHT: alto de la ventana (por ejemplo 800)
   - FPS: cuadros por segundo (por ejemplo 60)

2. Crea un segundo archivo `main.py` que importe esas constantes y
   muestre en consola la resolución y el FPS objetivo, usando un string:

   Resolución: {WIDTH}×{HEIGHT}, FPS objetivo: {FPS}

"""

# -----------------------------
# settings.py
# -----------------------------
import os

# Constantes de configuración
WIDTH  = 650
HEIGHT = 800
FPS    = 60

# -----------------------------
# main.py
# -----------------------------
from settings import WIDTH, HEIGHT, FPS

def main():
 print(f"Resolución: {WIDTH}×{HEIGHT}, FPS objetivo: {FPS}")

if __name__ == "__main__":
 main()
