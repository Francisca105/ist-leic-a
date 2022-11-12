def explode (numero):
    if type(numero) != int or numero < 0:
        raise ValueError("Tem de ser um numero inteiro positivo")
    tuplo = ()
    while numero > 0:
        tuplo += (numero % 10,)
        numero //= 10

    return tuplo[::-1]
    

#print(explode(34500))