# Ejercicio 3 Mejorado: Generación previa de la lista de índices

"""
Enunciado:
1. Genera primero una lista `indices` con los números del 1 al 12.
2. A partir de `indices`, crea `enemy_files_lc` usando list comprehension:
       enemy_files_lc = [f"asteroid{i}.gif" for i in indices]
3. A partir de `indices`, crea `enemy_files_loop` usando un bucle for y append:
       enemy_files_loop = []
       for i in indices:
           filename = "asteroid" + str(i) + ".gif"
           enemy_files_loop.append(filename)
4. Imprime `indices`, `enemy_files_lc` y `enemy_files_loop`, y comprueba que
   `enemy_files_lc == enemy_files_loop`.
"""

# -----------------------------
# Solución
# -----------------------------
# 1) Generación de la lista de índices
indices = list(range(1, 13))

# 2) Con list comprehension
enemy_files_lc = [f"asteroid{i}.gif" for i in indices]

# 3) Con bucle for y append
enemy_files_loop = []
for i in indices:
    filename = "asteroid" + str(i) + ".gif"
    enemy_files_loop.append(filename)

# 4) Comprobación
if __name__ == "__main__":
    print("Índices generados:", indices)
    print("Con comprehension:", enemy_files_lc)
    print("Con bucle for:   ", enemy_files_loop)
    print("¿Son iguales?    ", enemy_files_lc == enemy_files_loop)
