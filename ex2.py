def liste (a : float, b = 10) -> int :
    
    if a > b:
        return(f"Un des deux chiffres dépasse le seuil qui est de {b}")
    else:
        return a


print(liste(12,10))