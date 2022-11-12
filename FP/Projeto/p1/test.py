def limpa_texto(t):
    return  " ".join(t.split())

# def corta_texto(tex, num):
#     return (limpa_texto(tex[:num]), limpa_texto(tex[num:]))

def corta_texto(string, int):
    tuplo = string.split()
    length = 0
    res = ["", ""]
    extra = False

    for e in tuplo:
        lenE = len(e)
        if (length + lenE) <= int and not extra:
            length += lenE +1
            res[0] += f"{e} "
        else:
            extra = True
            res[1] += f"{e} "
    resultado = limpa_texto(res[0]), limpa_texto(res[1])

    return tuple(resultado)

#print(corta_texto("Fundamentos da Programacao", 15))

# def insere_espacos(string, int): # fala parte de +1 palavra
#     total_lenth = len(string)
#     tuplo = string.split()
#     palavras = len(tuplo)
#     valor = int-total_lenth
#     espacos = palavras-1
#     spaces = valor // espacos
#     length = 0
#     res = ""
#     i = 0

#     if palavras < 2:
#         return string + " "*(valor)

#     for e in tuplo:
#         lenE = len(e)
#         length += lenE
#         i+=1
#         print(e, spaces, int, palavras, total_lenth)
#         if i == 1:
#             res += e + " "*spaces
#         else:
#             res += " "*spaces + e
        
        
#     return res

# def insere_espacos(string, int): # falta verificar qnd n é divisível
#     res = ""
#     length = len(string.replace(" ",""))
#     split = string.split()
#     palavras = len(split)
#     espacos = int - length
#     if palavras == 1:
#         res = split[0] + " "*espacos
#         return res
#     add = espacos // (palavras - 1)
    
#     p = 0

#     for e in split:
#         p += 1
#         if p == palavras:            
#             res += e
#         elif p == 1 and espacos % (palavras - 1) != 0:
#             res += e + " "*(add+1)
#         else:
#             res += e + " "*add
#     return res



def insere_espacos(string, int): # falta verificar qnd n é divisível
    res = ""
    split = string.split()
    palavras = len(split)
    espacos = int - len(string.replace(" ",""))
    spaces = [0 for i in range(palavras-1)]

    if palavras == 1:
        res = split[0] + " "*espacos
        return res
    
    while espacos > 0:
        for i in range(len(spaces)):
            if espacos > 0:
                espacos -= 1
                spaces[i] += 1

    i = 0

    for p in split:
        if (i+1) == len(split):
            res += p
        else:
            res += p+" "*spaces[i]
        i+=1
    return res
        
def justifica_texto(string, inteiro):
    if not isinstance(string, str) or not isinstance(inteiro, int) or inteiro <= 0 or len(string) == 0:
        raise ValueError("justifica_texto: argumentos invalidos")
    for e in string.split():
        if len(e) > inteiro:
            raise ValueError("justifica_texto: argumentos invalidos")

    string = limpa_texto(string)
    res = ()
    cortado = corta_texto(string, inteiro)
    while cortado[1] != "":
        res += (insere_espacos(cortado[0], inteiro),)
        # print(cortado)
        cortado = corta_texto(cortado[1],inteiro)
        # print(cortado)
    res += (cortado[0] + " "*(inteiro - len(cortado[0])), )
    return res
