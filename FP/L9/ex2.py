def agrupa_por_chave(lista):
    dic = {}
    for p in lista:
        string = p[0]
        numero = [p[1]]
        if string in dic:
            dic[string] += numero
        else:
            dic[string] = numero

    return dic
print( agrupa_por_chave([("a", 8), ("b", 9), ("a", 3)]))