import pygame
import sys
import os
from settings import ASSETS_DIR, WIDTH, HEIGHT, FPS, GREEN, WHITE
from utils import draw_text

# Valores inyectados desde main.py
screen = None
clock = None
font_name = None

def show_menu():
    bg = pygame.image.load(os.path.join(ASSETS_DIR, "menu_background.png")).convert_alpha()
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
    btn_w, btn_h = 200, 50
    play_btn = pygame.Rect((WIDTH-btn_w)//2, HEIGHT//2-40, btn_w, btn_h)
    exit_btn = pygame.Rect((WIDTH-btn_w)//2, HEIGHT//2+20, btn_w, btn_h)
    btn_font = pygame.font.Font(font_name, 36)

    while True:
        clock.tick(FPS)
        mx, my = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    return
                if e.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if play_btn.collidepoint(e.pos):
                    return
                if exit_btn.collidepoint(e.pos):
                    pygame.quit(); sys.exit()

        screen.blit(bg, (0, 0))
        draw_text(screen, "Space Ship", 64, WIDTH//2, HEIGHT//4)

        color = GREEN if not play_btn.collidepoint((mx, my)) else (0,200,0)
        pygame.draw.rect(screen, color, play_btn, border_radius=8)
        txt1 = btn_font.render("JUGAR", True, WHITE)
        screen.blit(txt1, txt1.get_rect(center=play_btn.center))

        color = GREEN if not exit_btn.collidepoint((mx, my)) else (0,200,0)
        pygame.draw.rect(screen, color, exit_btn, border_radius=8)
        txt2 = btn_font.render("SALIR", True, WHITE)
        screen.blit(txt2, txt2.get_rect(center=exit_btn.center))

        pygame.display.flip()
