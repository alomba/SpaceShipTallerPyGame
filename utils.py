import pygame
from settings import WHITE, RED, GREEN

# Nombre de fuente asignado en main.py
font_name = None

# =============================
# 2. FUNCIONES AUXILIARES
# =============================
def draw_text(surface, text, size, x, y, color=WHITE):
    """
    Dibuja texto centrado en (x, y).
    surface: pantalla o Surface de Pygame
    text: cadena a mostrar
    size: tamaño de fuente en puntos
    color: color RGB
    """
    font = pygame.font.Font(font_name, size)
    txt_surf = font.render(text, True, color)
    txt_rect = txt_surf.get_rect(center=(x, y))
    surface.blit(txt_surf, txt_rect)

def draw_score(surface, text, size, pos):
    """
    Muestra la puntuación con sombra roja.
    pos: (x, y) de la parte superior central del texto
    """
    font = pygame.font.Font(font_name, size)
    surf = font.render(text, True, WHITE)
    shadow = font.render(text, True, RED)
    rect = surf.get_rect(midtop=pos)
    surface.blit(shadow, (rect.x + 2, rect.y + 2))
    surface.blit(surf, rect)

def draw_health_bar(surface, x, y, pct):
    """
    Dibuja la barra de salud en (x, y).
    pct: porcentaje de vida (0–100)
    """
    if pct < 0:
        pct = 0
    BAR_LEN, BAR_H = 100, 10
    fill = (pct / 100) * BAR_LEN
    pygame.draw.rect(surface, RED,   (x, y, BAR_LEN, BAR_H))
    pygame.draw.rect(surface, GREEN, (x, y, fill, BAR_H))
    pygame.draw.rect(surface, WHITE, (x, y, BAR_LEN, BAR_H), 1)
