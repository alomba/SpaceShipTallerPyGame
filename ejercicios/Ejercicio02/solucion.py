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
