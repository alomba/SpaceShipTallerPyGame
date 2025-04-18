import pygame
import sys
import random
from settings import WIDTH, HEIGHT, FPS, BLACK
from utils import draw_score, draw_health_bar
from sprites import Player, Mob, Bullet, Explosion

# Valores inyectados desde main.py
screen = None
clock = None
background = None
background_rect = None
snd_explosions = None

def new_mob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

def run_game():
    global all_sprites, mobs, bullets
    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    # Inyectar grupos en sprites para Player.shoot()
    import sprites
    sprites.all_sprites = all_sprites
    sprites.bullets = bullets

    player = Player()
    all_sprites.add(player)
    for _ in range(8):
        new_mob()

    score = 0
    running = True
    death_exp = None

    while running:
        clock.tick(FPS)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                player.shoot()

        all_sprites.update()

        hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
        for hit in hits:
            snd_explosions[0].play()
            exp = Explosion(hit.rect.center, 'small')
            all_sprites.add(exp)
            player.health -= 25
            new_mob()
            if player.health <= 0 and death_exp is None:
                death_exp = Explosion(player.rect.center, 'player')
                all_sprites.add(death_exp)
                player.kill()
        if death_exp and not death_exp.alive():
            running = False

        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:
            random.choice(snd_explosions).play()
            exp = Explosion(hit.rect.center, 'big')
            all_sprites.add(exp)
            score += 25
            new_mob()

        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        draw_score(screen, str(score), 18, (WIDTH//2, 10))
        draw_health_bar(screen, 5, 5, player.health)
        pygame.display.flip()
