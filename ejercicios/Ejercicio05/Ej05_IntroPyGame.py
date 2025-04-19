# Ejercicio 5: Bucle principal de Pygame

"""
Enunciado:
1. Escribe un script `main.py` que:
   - Importe pygame y sys.
   - Importe las constantes WIDTH, HEIGHT, FPS desde `settings.py`.
2. En la función `main_loop()`:
   - Inicializa pygame con `pygame.init()`.
   - Crea una ventana de tamaño (WIDTH, HEIGHT).
   - Crea un clock con `pygame.time.Clock()`.
   - Ejecuta un bucle `while running` que:
     * Llama a `clock.tick(FPS)` para controlar la velocidad.
     * Recorre `pygame.event.get()` y, si hay un evento QUIT, sale del bucle.
     * Rellena la pantalla de color negro y hace `pygame.display.flip()`.
   - Al salir, llama a `pygame.quit()` y `sys.exit()`.
3. Ejecuta `main_loop()` cuando el script se llame directamente.
"""

# -----------------------------
# main.py
# -----------------------------
import pygame
import sys
from settings import WIDTH, HEIGHT, FPS

def main_loop():
    # Inicializar Pygame
    pygame.init()
    # Crear ventana y clock
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bucle Pygame")
    clock = pygame.time.Clock()

    running = True
    while running:
        # Control de FPS
        clock.tick(FPS)

        # Gestión de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Pintar fondo negro
        screen.fill((0, 0, 0))
        # Actualizar pantalla
        pygame.display.flip()

    # Salida limpia
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_loop()
