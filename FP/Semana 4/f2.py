# Definir uma função que recebe um número e um dígito e que devolve o número escrito mas só com os algarismos q são múltiplos do digito. (Só podes usar matéria do capítulo das funções)
# Ex: 234567 e 8
# 24


def check (numero, digito):
    tuplo = ()
    while numero > 0:
        tuplo += (numero % 10, )
        numero //= 10
    tuplo = tuplo[::-1]

    res = 0

    for i in tuplo:
        if i % digito == 0 or digito % i == 0:
            res = res*10 + i

    return res


print(check(234567, 8))