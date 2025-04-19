import pygame

class SimpleSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()  # Inicializa la parte base de Sprite
        # Creamos la imagen: 50×50 y la rellenamos de rojo
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        # Obtenemos el rect y lo posicionamos
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        # Mover un píxel a la derecha
        self.rect.x += 1

# Prueba de funcionamiento
if __name__ == "__main__":
    # Sin inicializar toda la pantalla, comprobamos solo textura y rect
    sprite = SimpleSprite(10, 20)
    print("Posición inicial:", sprite.rect.topleft)
    for i in range(5):
        sprite.update()
        print(f"Tras update {i+1}:", sprite.rect.topleft)