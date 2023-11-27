def chiffrement_cesar(message, decalage):
    resultat = ""
    for char in message:
        # Vérifier si le caractère est une lettre
        if char.isalpha():
            # Déterminer si le caractère est en majuscule ou en minuscule
            est_majuscule = char.isupper()
            
            # Appliquer le décalage en prenant en compte le dépassement
            code = ord(char) + decalage
            if est_majuscule:
                if code > ord('Z'):
                    code -= 26
                elif code < ord('A'):
                    code += 26
            else:
                if code > ord('z'):
                    code -= 26
                elif code < ord('a'):
                    code += 26
            
            # Ajouter le caractère décalé au résultat
            resultat += chr(code)
        else:
            # Si le caractère n'est pas une lettre, ajouter tel quel
            resultat += char

    return resultat

# Exemple d'utilisation avec un message et un décalage de 3
message = "Hello, World!"
decalage = 3
message_chiffre = chiffrement_cesar(message, decalage)

print("Message original:", message)
print("Message chiffré:", message_chiffre)