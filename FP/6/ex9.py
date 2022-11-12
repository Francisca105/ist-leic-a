def num_occ_lista(lista: list, dig: int):
    res = 0
    for e in lista:
        if type(e) != list:
            if e == dig:
                res += 1
        else:
            res += num_occ_lista(e, dig)
    return res