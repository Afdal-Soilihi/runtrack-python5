def draw_triangle(height):
    if height < 1:
        print("La hauteur doit être d'au moins 1.")
        return

    # Dessiner les lignes du triangle
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        if i == 1:
            print(spaces + "_")
        elif i == height:
            print("/" + "_" * (2 * (i - 1)) + "\\")
        else:
            print(spaces + "/" + " " * (2 * (i - 1) - 1) + "\\")

# Appel de la fonction avec height=5
draw_triangle(5)