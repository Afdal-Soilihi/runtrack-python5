def draw_rectangle(width, height):
    if width < 2 or height < 2:
        print("Les dimensions doivent être supérieures à 1.")
        return

    # Dessiner la première ligne du rectangle
    print("|" + "-" * (width - 2) + "|")

    # Dessiner les lignes intérieures
    for _ in range(height - 2):
        print("|" + " " * (width - 2) + "|")

    # Dessiner la dernière ligne du rectangle
    print("|" + "-" * (width - 2) + "|")

# Exemple d'utilisation avec width=10 et height=3
draw_rectangle(10, 3)