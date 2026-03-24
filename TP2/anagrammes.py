def est_anagramme(s, t):
    if len(s) != len(t):
        return False

    if sorted(s) == sorted(t):
        return True
    else:
        return False
    
print(est_anagramme("python", "onhtyp"))  # True
print(est_anagramme("tp", "tps"))        # False