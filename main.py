#!/usr/bin/env python3
import pygame
import sys
import os
from settings import *
import utils
import sprites
import menu
import game

def main():
    # Inicializar Pygame
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    pygame.mixer.init()

    # Cargar y reproducir música de fondo
    pygame.mixer.music.load(os.path.join(ASSETS_DIR, "Venus.wav"))
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(loops=-1)

    # Configurar pantalla y reloj
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("CodeCAN - Taller Pygame - Space Ship")
    clock = pygame.time.Clock()
    font_name = pygame.font.match_font('arial')

    # Inyectar en utils
    utils.font_name = font_name

    # Cargar assets
    background_raw = pygame.image.load(os.path.join(ASSETS_DIR, "starfield.png")).convert_alpha()
    background = pygame.transform.scale(background_raw, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    player_img = pygame.image.load(os.path.join(ASSETS_DIR, "player.png")).convert_alpha()
    enemy_files = [f"asteroid{i}.gif" for i in range(1, 13)]
    enemy_images = [pygame.image.load(os.path.join(ASSETS_DIR, f)).convert_alpha() for f in enemy_files]
    bullet_img = pygame.image.load(os.path.join(ASSETS_DIR, "bullet.png")).convert_alpha()

    explosion_anim = {'big': [], 'small': []}
    for i in range(3):
        frame = pygame.image.load(os.path.join(ASSETS_DIR, f"explosion{i}.png")).convert_alpha()
        explosion_anim['big'].append(pygame.transform.scale(frame, (32, 32)))
        explosion_anim['small'].append(frame)
    explosion_anim['player'] = explosion_anim['big'][:3] + [explosion_anim['big'][1], explosion_anim['big'][0]]

    snd_shoot = pygame.mixer.Sound(os.path.join(ASSETS_DIR, "laser_shoot.wav"))
    snd_shoot.set_volume(0.1)
    snd_explosions = []
    for fn in ["explosion.wav", "explosion2.wav", "explosion3.wav"]:
        s = pygame.mixer.Sound(os.path.join(ASSETS_DIR, fn))
        s.set_volume(0.04)
        snd_explosions.append(s)

    # Inyectar en sprites
    sprites.player_img = player_img
    sprites.enemy_images = enemy_images
    sprites.bullet_img = bullet_img
    sprites.explosion_anim = explosion_anim
    sprites.snd_shoot = snd_shoot

    # Inyectar en menu
    menu.screen = screen
    menu.clock = clock
    menu.font_name = font_name

    # Inyectar en game
    game.screen = screen
    game.clock = clock
    game.background = background
    game.background_rect = background_rect
    game.snd_explosions = snd_explosions

    # Bucle principal: menú → juego
    while True:
        menu.show_menu()
        game.run_game()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
