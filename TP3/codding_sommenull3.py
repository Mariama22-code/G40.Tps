def somme_nulle_trois(tab):
    n = len(tab)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if tab[i] + tab[j] + tab[k] == 0:
                    return [tab[i], tab[j], tab[k]]

    return None


entree = input("EX2:Entrez des nombres séparés par des espaces : ")
tab = list(map(int, entree.split()))

resultat = somme_nulle_trois(tab)

if resultat:
    print("Triplet trouvé :", resultat)
else:
    print("Aucun triplet de somme nulle trouvé.")