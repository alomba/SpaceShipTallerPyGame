SpaceShipProject_Modular/
├── assets/              ← Carpeta con imágenes y sonidos usados por el juego
│   ├── player.png
│   ├── starfield.png
│   ├── menu_background.png
│   ├── bullet.png
│   ├── asteroid1.gif … asteroid12.gif
│   ├── explosion0.png … explosion2.png
│   └── Venus.wav, laser_shoot.wav, explosion.wav…
│
├── settings.py          ← Constantes globales (tamaño ventana, FPS, colores, rutas)
│
├── utils.py             ← Funciones generales: dibujar texto, marcador y barra de vida
│
├── sprites.py           ← Clases de los objetos del juego (Player, Mob, Bullet, Explosion)
│
├── menu.py              ← Lógica y renderizado del menú inicial (mostrar, detectar clics/teclas)
│
├── game.py              ← Bucle de la partida: creación de niveles, colisiones, puntuación y dibujo
│
└── main.py              ← Punto de entrada: inicializa Pygame, carga assets, inyecta dependencias y lanza menú/juego

Descripción de los principales módulos:

    assets/
    Carpeta que debes mantener paralela al código. Incluye todos los archivos multimedia (imágenes en PNG/GIF y sonidos en WAV/OGG).

    settings.py
    Centraliza valores “mágicos”:

        WIDTH, HEIGHT, FPS

        Colores RGB (BLACK, WHITE, RED, …)

        MAX_BULLETS

        Ruta ASSETS_DIR

    utils.py
    Funciones reutilizables de dibujo:

        draw_text() para texto centrado

        draw_score() para marcador con sombra

        draw_health_bar() para la barra de vida

    sprites.py
    Define las clases que heredan de pygame.sprite.Sprite:

        Player (movimiento, disparo)

        Mob (asteroides con rotación y caída)

        Bullet (proyectiles)

        Explosion (animaciones de explosión)

    menu.py
    Función show_menu() que:

        Carga y escala fondo

        Dibuja título y botones

        Espera ENTER/Esc o clics para avanzar o salir

    game.py
    Función run_game() que:

        Configura grupos de sprites

        Gestiona eventos (movimiento, disparo, cierre)

        Detecta colisiones (nave–asteroide, bala–asteroide)

        Actualiza estado (vida, puntuación)

        Dibuja fondo, sprites y HUD

    main.py
    Orquesta todo:

        Inicializa Pygame y sonidos

        Carga assets y asigna variables a módulos

        Bucle principal: show_menu() → run_game()