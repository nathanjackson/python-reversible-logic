def toffoli(a, b, c):
    return a, b, c ^ (a & b)


def reversible_and(a, b):
    return toffoli(a, b, False)

print(reversible_and(False, False))

