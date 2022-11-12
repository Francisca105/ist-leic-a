d = {}

print(d == dict())

def limpa_texto(string):
    return " ".join(string.split())

def corta_texto(string, int):
    tuplo = string.split()
    length = 0
    primeiro, segundo = (), ()

    for e in tuplo:
        lenE = len(e)
        if (length + lenE) < int:
            length += lenE
            primeiro += (e, )
        else:
            segundo +=(e,)
    return primeiro, segundo

def insere_espacos(string, int): # fala parte de +1 palavra
    total_lenth = len(string)

    print(total_lenth)
    tuplo = string.split()
    palavras = len(tuplo)
    length = 0
    if palavras < 2:
        return string + " "*(int-total_lenth)

    for e in tuplo:
        lenE = len(e)
        length += lenE
        print(lenE, length)
    return