# Space Ship

Juego de disparos espacial desarrollado con Pygame, organizado de forma modular para facilitar su comprensión y mantenimiento.

## 🚀 Características

- **Nave Jugadora:** controlada con las flechas del teclado y dispara con la barra espaciadora.
- **Enemigos:** asteroides que caen desde la parte superior con rotación aleatoria.
- **Proyectiles:** limitados a un disparo activo para evitar spam.
- **Explosiones Animadas:** en dos tamaños (pequeño y grande) y efecto especial para la nave.
- **Interfaz (HUD):** marcador de puntuación y barra de vida con indicadores visuales.
- **Menú Inicial:** pantalla de bienvenida con opciones de Jugar y Salir.
- **Audio:** música de fondo y efectos de disparo/explosión.

## 📂 Estructura del Proyecto

```
SpaceShipProject_Modular/
├── assets/              # Imágenes (.png, .gif) y sonidos (.wav)
├── settings.py          # Constantes globales y rutas
├── utils.py             # Funciones de dibujo (texto, marcador, salud)
├── sprites.py           # Clases de objetos del juego
├── menu.py              # Lógica y renderizado del menú inicial
├── game.py              # Bucle de partida: eventos, colisiones, HUD
└── main.py              # Punto de entrada: inicialización y bucle principal
```

## ⚙️ Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/SpaceShipProject_Modular.git
cd SpaceShipProject_Modular
```
2. Asegúrate de tener la carpeta `assets/` con todos los archivos multimedia.
3. Instala Pygame:
   ```bash
pip install pygame
```

## ▶️ Uso

Ejecuta el juego con:

```bash
python main.py
```

- **Iniciar Menú:** usa ENTER o clic en "JUGAR".
- **Controles del Juego:**
  - Flechas ◀▲▶▼ para mover la nave.
  - Barra espaciadora para disparar.
- **Salir:** ESC en menú o cerrar la ventana.

## 📝 Módulos Principales

- **settings.py:** configuración global (dimensiones, FPS, colores, rutas).
- **utils.py:** funciones reutilizables para renderizar texto, marcador y barra de vida.
- **sprites.py:** definición de clases `Player`, `Mob`, `Bullet` y `Explosion`.
- **menu.py:** implementación de `show_menu()` con lógica de botones.
- **game.py:** implementación de `run_game()` con bucle de eventos, colisiones y dibujo.
- **main.py:** inicialización de Pygame, carga de recursos, inyección de dependencias y bucle principal.


## 📄 Licencia

Proyecto bajo licencia **MIT** © 2025 Ayose Lomba Pérez

