import pygame
import random
from settings import WIDTH, HEIGHT, MAX_BULLETS

# Imágenes y sonidos asignados en main.py
player_img = None
enemy_images = None
bullet_img = None
explosion_anim = None
snd_shoot = None

# Grupos de sprites asignados en game.py
all_sprites = None
bullets = None

# =============================
# 3. CLASES PRINCIPALES
# =============================
class Player(pygame.sprite.Sprite):
    """Nave del jugador con movimiento y disparo."""
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(midbottom=(WIDTH//2, HEIGHT-10))
        self.speedx = self.speedy = 0
        self.health = 100

    def update(self):
        """Movimiento con flechas y límites de pantalla."""
        self.speedx = self.speedy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speedx = -5
        if keys[pygame.K_RIGHT]:
            self.speedx = 5
        if keys[pygame.K_UP]:
            self.speedy = -5
        if keys[pygame.K_DOWN]:
            self.speedy = 5
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

    def shoot(self):
        """Dispara un proyectil si no supera MAX_BULLETS."""
        if len(bullets) < MAX_BULLETS:
            snd_shoot.play()
            b = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(b)
            bullets.add(b)

class Mob(pygame.sprite.Sprite):
    """Asteroide enemigo que rota y cae."""
    def __init__(self):
        super().__init__()
        self.original = random.choice(enemy_images)
        self.image = self.original.copy()
        self.rect = self.image.get_rect(
            x=random.randint(0, WIDTH-self.image.get_width()),
            y=random.randint(-100, -60)
        )
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randint(-1, 1)
        self.rot = 0
        self.rot_speed = random.uniform(-5, 5)
        self.last_time = pygame.time.get_ticks()

    def rotate(self):
        """Rota la imagen cada 50 ms, manteniendo el centro."""
        now = pygame.time.get_ticks()
        if now - self.last_time > 50:
            self.last_time = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_img = pygame.transform.rotate(self.original, self.rot)
            center = self.rect.center
            self.image = new_img
            self.rect = self.image.get_rect(center=center)

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        # Reposicionar si sale de pantalla
        if (self.rect.top > HEIGHT+10 or
            self.rect.left < -self.rect.width or
            self.rect.right > WIDTH+self.rect.width):
            self.rect.x = random.randint(0, WIDTH-self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speedy = random.randrange(1, 8)
            self.speedx = random.randint(-1, 1)
            self.rot_speed = random.uniform(-5, 5)

class Bullet(pygame.sprite.Sprite):
    """Proyectil que sube y se destruye al salir."""
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect(center=(x, y))
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    """Animación de explosión basada en frames."""
    def __init__(self, center, size):
        super().__init__()
        self.frames = explosion_anim[size]
        self.frame = 0
        self.image = self.frames[self.frame]
        self.rect = self.image.get_rect(center=center)
        self.last_time = pygame.time.get_ticks()
        self.delay = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_time > self.delay:
            self.last_time = now
            self.frame += 1
            if self.frame >= len(self.frames):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.frames[self.frame]
                self.rect = self.image.get_rect(center=center)
