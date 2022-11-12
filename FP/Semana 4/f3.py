# (Já podes usar Tuplos) defense uma função que recebe um tuplo, com números inteiros ou floats e pelo menos dois números, e que entre cada par de números escreve os sinais <, > ou =.
# Ex: t = (1, 3, 2, 2, 9)
# (1, <, 3, >, 2, =, 2, <, 9)

def comparar (tuplo):
    if len(tuplo) < 2 or type(tuplo) != tuple:
        raise ValueError("Argumento invalido")

    res = ()
    i = 0
    length = len(tuplo)
    for element in tuplo:
        if type(element) != float and type(element) != int:
            raise ValueError("Argumento invalido")

        if (i+1) == length:
            res += (element,)
            return res
        next = tuplo[i+1]

        if element > next:
            res += (element, '>',)
        elif element < next:
            res += (element, '<',)
        else:
            res += (element, '=',)

        i+=1

print(comparar((1, 3, 2, 2, 9)))