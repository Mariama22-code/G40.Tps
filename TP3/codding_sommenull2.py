def somme_nulle_deux(tab):
    vus = set()

    for x in tab:
        if -x in vus:
            return [x, -x]
        vus.add(x)

    return None


entree = input("EXO1 :Entrez des nombres séparés par des espaces : ")
tab = list(map(int, entree.split()))

resultat = somme_nulle_deux(tab)

if resultat:
    print("Couple trouvé :", resultat)
else:
    print("Aucun couple de somme nulle trouvé.")
