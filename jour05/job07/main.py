def arrondir_notes(notes):
    notes_arrondies = []
    
    for note in notes:
        if note < 40:
            notes_arrondies.append(note)  # Échec, pas d'arrondi
        else:
            multiple_de_5_superieur = (note // 5 + 1) * 5
            difference = multiple_de_5_superieur - note
            
            if difference < 3:
                notes_arrondies.append(multiple_de_5_superieur)
            else:
                notes_arrondies.append(note)  # Pas d'arrondi
                
    return notes_arrondies

# Exemple d'utilisation avec une liste de notes
liste_notes = [83, 82, 45, 38, 91, 56]
notes_arrondies = arrondir_notes(liste_notes)

# Affichage du résultat
for i in range(len(liste_notes)):
    print(f"Note originale : {liste_notes[i]}, Note arrondie : {notes_arrondies[i]}")