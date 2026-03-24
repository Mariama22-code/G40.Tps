def contient_doublon(t):
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            if t[i] == t[j]:
                return True
    return False

t = [1, 2, 3, 1]
print(contient_doublon(t)) 