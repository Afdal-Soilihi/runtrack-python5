def distance_toilettes_par_semaine(nombre_marches, hauteur_marche):
    nombre_jours_semaine = 7
    nombre_allers_retours_par_jour = 2
    hauteur_marches_cm = nombre_marches * hauteur_marche
    hauteur_marches_m = hauteur_marches_cm / 100  # Conversion en mètres
    distance_totale_m = hauteur_marches_m * nombre_allers_retours_par_jour * nombre_jours_semaine

    return distance_totale_m

# Exemple d'utilisation avec 100 marches de 20 cm chacune
nombre_marches = 100
hauteur_marche = 20
distance_totale = distance_toilettes_par_semaine(nombre_marches, hauteur_marche)

# Affichage du résultat
print(f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_totale:.2f} m par semaine.")