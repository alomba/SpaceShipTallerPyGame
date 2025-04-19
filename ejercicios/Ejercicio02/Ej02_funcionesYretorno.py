# Ejercicio 2: Funciones y retorno

"""
Enunciado:
1. Crea una función `format_score(text)`.
2. Esta función debe:
   - Recibir un número o cadena `text`.
   - Devuelver una cadena formateada: "Puntuación: <text>".
3. Prueba la función con diferentes valores.
"""

# -----------------------------
# Solución propuesta
# -----------------------------
def format_score(text):
    """
    Devuelve una cadena con la puntuación formateada.
    """
    return f"Puntuación: {text}"

# Pruebas de la función
if __name__ == "__main__":
    print(format_score(123))    # → Puntuación: 123
    print(format_score("250"))  # → Puntuación: 250
    print(format_score(0))      # → Puntuación: 0
