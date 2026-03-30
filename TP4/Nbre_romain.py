def romain_vers_entier(s):
    valeurs = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(s)):
        if i + 1 < len(s) and valeurs[s[i]] < valeurs[s[i+1]]:
            result -= valeurs[s[i]]
        else:
            result += valeurs[s[i]]
    return result

print(romain_vers_entier('III'))      # 3
print(romain_vers_entier('MCMXCIV')) # 1994