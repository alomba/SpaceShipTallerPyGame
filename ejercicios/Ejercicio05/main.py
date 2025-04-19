# -----------------------------
# main.py
# -----------------------------

import pygame   # Motor de juegos 2D: gráficos, sonido y entrada
import sys      # Para salir limpiamente de la aplicación
from settings import WIDTH, HEIGHT, FPS  # Constantes de configuración

def main_loop():
    """
    Función principal que configura Pygame y ejecuta el bucle de juego.
    """
    # Inicializa todos los módulos de Pygame (gráficos, audio, etc.)
    pygame.init()

    # Crea la ventana con el tamaño especificado en WIDTH y HEIGHT
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # Establece el título de la ventana
    pygame.display.set_caption("Bucle Pygame")

    # Crea un reloj para controlar la velocidad de refresco (frames por segundo)
    clock = pygame.time.Clock()

    # Variable de control del bucle principal
    running = True

    # Bucle principal: se repite hasta que `running` sea False
    while running:
        # Limita la velocidad del bucle a FPS cuadros por segundo
        # Evita que el juego se ejecute demasiado rápido
        clock.tick(FPS)

        # Proceso de la cola de eventos de Pygame
        # Aquí leemos pulsaciones de teclas, movimientos de ratón, cerrar ventana...
        for event in pygame.event.get():
            # Si detectamos que el usuario cierra la ventana, paramos el bucle
            if event.type == pygame.QUIT:
                running = False

        # Limpia la pantalla pintando un fondo negro
        # `screen.fill()` rellena toda la superficie con el color indicado
        screen.fill((0, 0, 0))

        # `pygame.display.flip()` actualiza toda la ventana con lo que esté
        # dibujado en `screen` hasta este momento
        pygame.display.flip()

    # Al salir del bucle, limpiamos y cerramos Pygame correctamente
    pygame.quit()
    # Termina la ejecución del programa
    sys.exit()

# Si este script se ejecuta directamente (no importado), lanzamos main_loop()
if __name__ == "__main__":
    main_loop()
