def remove_multiplos(lista, dig):
    res = []
    for e in lista:
        if e % dig != 0:
            res.append(e)
    return res