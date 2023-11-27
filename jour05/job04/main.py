def draw_diagonal_carpet(n):
    for i in range(n + 1):
        for j in range(n + 1):
            if i == j:
                print("/", end="")
            elif i + j == n:
                print("\\", end="")
            else:
                print("#", end="")
        print()  # Passer à la ligne suivante après chaque ligne

# Appel de la fonction avec n=10
draw_diagonal_carpet(10)