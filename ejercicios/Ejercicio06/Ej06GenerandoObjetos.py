# Ejercicio 6: Generación de objetos con función genérica

"""
Enunciado:
1. Crea una función `new_object(group, cls, *args, **kwargs)` que:
   - Instancie `cls(*args, **kwargs)`.
   - Añada esa instancia al grupo `group` (que debe tener método `.add()`).
   - Devuelva la instancia creada.

2. Muestra cómo llamar a `new_object()` para crear un `Mob`
   y añadirlo al grupo `all_sprites`.
"""

def new_object(group, cls, *args, **kwargs):
    """
    Crea una instancia de cls con los argumentos dados,
    la añade a 'group' y devuelve la instancia.
    """
    instance = cls(*args, **kwargs)
    group.add(instance)
    return instance

# -----------------------------
# Ejemplo de uso (suponiendo Pygame cargado y sprites.py disponible)
# -----------------------------
if __name__ == "__main__":
    import pygame
    from sprites import Mob

    # Inicializamos Pygame mínimo para usar Group
    pygame.init()
    group = pygame.sprite.Group()

    # Creamos un Mob y lo añadimos al grupo
    mob = new_object(group, Mob)
    
    # Verificamos
    print("Tipo de objeto:", type(mob))
    print("Miembros del grupo:", list(group))
