def soma_cumulativa(lista):
    soma = 0
    res = []
    for e in lista:
        soma += e
        res.append(soma)
    return res