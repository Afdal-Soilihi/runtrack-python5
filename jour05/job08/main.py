def my_sort(lst):
    n = len(lst)
    coups = 0
    trie = False

    while not trie:
        trie = True  # Supposons que la liste est triée

        for i in range(n - 1):
            if lst[i] > lst[i + 1]:
                # Échangez les éléments
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                trie = False  # La liste n'est pas encore triée
                coups += 1

    print(f"Nombre total de coups nécessaires pour trier la liste : {coups}")
    return lst

# Exemple d'utilisation avec une liste non triée
ma_liste = [4, 2, 7, 1, 9, 3]
liste_triee = my_sort(ma_liste.copy())  # Copy pour ne pas modifier la liste originale

# Affichage du résultat
print("Liste triée :", liste_triee)