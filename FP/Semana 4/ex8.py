def junta_ordenados(tuplo1, tuplo2):
    tuplo = tuplo1 + tuplo2
    return tuple(sorted(tuplo))

print( junta_ordenados((2, 34, 200, 210), (1, 23)) )
