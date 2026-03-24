def somme_nulle_deux(tab):
    for i in range(len(tab)):
        for j in range(i + 1, len(tab)):
            if tab[i] + tab[j] == 0:
                return [tab[i], tab[j]]
    return None


entree = input("EXO1 : Entrez des nombres séparés par des espaces : ")
tab = list(map(int, entree.split()))

resultat = somme_nulle_deux(tab)

if resultat:
    print("Couple trouvé :", resultat)
else:
    print("Aucun couple de somme nulle trouvé.")
