def valor(q, j, n): 
    if isinstance(q, int) and q > 0 and isinstance(j, int) and 1 > j > 0 and isinstance(n, int) and n > 0:
        raise ValueError("Argumentos incorretos")

    return q * (1+j)**n

#print(valor(100, 0.03, 24))

def duplicar(q, j):
    if isinstance(q, int) and q > 0 and isinstance(j, int) and 1 > j > 0:
        raise ValueError("Argumentos incorretos")

    ano = 1
    double = q * 2

    while valor(q,j,ano) < double:
        ano += 1
    return ano

#print(duplicar(100,0.03))