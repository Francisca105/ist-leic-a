from ex2 import explode
from ex3 import implodeFor
from ex4 import filtra_pares

def algarismos_pares(numero):
    if type(numero) != int:
        raise ValueError("elemento não inteiro")
    return implodeFor(filtra_pares(explode(numero)))

print( algarismos_pares(6643399766641) )