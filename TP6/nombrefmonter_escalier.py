def escaliers(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return escaliers(n-1) + escaliers(n-2)

print(escaliers(4))  # résultat : 5