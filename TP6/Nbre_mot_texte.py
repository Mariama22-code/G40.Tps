def nombre_mots(texte):
    mots = texte.split()
    return len(mots)

print(nombre_mots("Bonjour tout le monde, commencez à coder."))