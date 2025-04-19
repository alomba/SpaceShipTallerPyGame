# -----------------------------
# sprites.py
# -----------------------------
import pygame
import random
from settings import WIDTH, HEIGHT

class Mob(pygame.sprite.Sprite):
    """
    Sprite sencillo que aparece en posición aleatoria
    y se desplaza hacia abajo en cada update().
    """
    def __init__(self, x=None, y=None):
        super().__init__()
        # Creamos una superficie de 30×30 pixels, color rojo
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        # Posición inicial: aleatoria si no se pasa x/y
        self.rect.x = random.randint(0, WIDTH - self.rect.width) if x is None else x
        self.rect.y = random.randint(0, HEIGHT - self.rect.height) if y is None else y

    def update(self):
        # Moverse 1 píxel hacia abajo
        self.rect.y += 1
        # Si sale de abajo, reaparece arriba
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
