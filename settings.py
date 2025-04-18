import os

# =============================
# 1. CONFIGURACIÓN GLOBAL
# =============================
WIDTH = 650           # Ancho de la ventana en píxeles
HEIGHT = 800          # Alto de la ventana en píxeles
FPS = 60              # Cuadros por segundo

# Colores en formato RGB
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
RED    = (255,   0,   0)
YELLOW = (200, 190,  16)
GREEN  = (  0, 255,   0)

MAX_BULLETS = 1  # Máximo de proyectiles simultáneos

# Ruta de la carpeta 'assets'
ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
