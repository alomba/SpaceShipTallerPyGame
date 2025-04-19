# -----------------------------
# main.py
# -----------------------------
import pygame
import sys
from settings import WIDTH, HEIGHT, FPS, BG_COLOR
from sprites import Mob


def new_object(group, cls, *args, **kwargs):
    """
    Crea una instancia de cls(*args, **kwargs), la añade a group
    y devuelve la instancia.
    """
    instance = cls(*args, **kwargs)
    group.add(instance)
    return instance


def main():
    # Inicializar Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ejercicio 6: new_object")
    clock = pygame.time.Clock()

    # Crear un group para sprites
    all_sprites = pygame.sprite.Group()
    # Usar new_object para instanciar y añadir un Mob
    mob = new_object(all_sprites, Mob)

    running = True
    while running:
        # Control de FPS
        clock.tick(FPS)
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Actualizar sprites
        all_sprites.update()

        # Dibujar fondo y sprites
        screen.fill(BG_COLOR)
        all_sprites.draw(screen)
        pygame.display.flip()

    # Salir limpiamente
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
