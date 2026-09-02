liste = [1, 2, 3, 8, 4]

def fcompt(liste, seuil=3):
    compteur = 0
    for element in liste:
        if element < seuil:
            compteur += 1
    return compteur

print(fcompt())
