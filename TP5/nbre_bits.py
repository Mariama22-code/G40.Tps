def nombre_bits_un(n):
    compteur = 0
    while n > 0:
        if n & 1 == 1:
            compteur += 1
        n = n >> 1
    return compteur

def test_unitaire():
    assert nombre_bits_un(7)  == 3
    assert nombre_bits_un(10) == 2
    print("Tous les tests sont passes !")

if __name__ == '__main__':
    test_unitaire()
    print(nombre_bits_un(7))
    print(nombre_bits_un(10))