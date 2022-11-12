def serie_geom(r,n):
    if n < 0:
        raise ValueError("arg incorreto")

    i = 0
    soma = 0
    while n >= i:
        soma += r**i
        i+=1
    return soma

print(serie_geom(-100,10))