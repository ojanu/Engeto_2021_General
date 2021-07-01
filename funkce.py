def sum_range(start, stop):
    vysledek = 0
    for i in range(start, stop):
        vysledek += i
    return vysledek


soucet = sum_range(1, 10)

print(soucet)
