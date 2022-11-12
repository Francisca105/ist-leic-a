def calcula_quocientes(circulo, n):
    i = 1
    resultado = {p: [] for p in circulo}
    while n >= i:
        for p in circulo:
            resultado[p].append(circulo[p] / i)
        i+=1
    return resultado

def atribui_mandatos(circulo, n):
    valores = calcula_quocientes(circulo, n)
    res = []
    while n > 0:
        maximo = max(valores, key=valores.get)
        value = maximo
        for p in valores:
            if p != maximo and  valores[p][0] == valores[maximo][0] and res.count(maximo) > res.count(p):
                value = p

        res.append(value)
        del valores[value][0]
        n -= 1
    return res

# info = {
#     "Endor": {"deputados": 7,"votos": {"A":12000, "B":7500, "C":5250, "D":3000}},
#     "Hoth": {"deputados": 6,"votos": {"B":11500, "A":9000, "E":5000, "D":1500}},
#     "Tatooine": {"deputados": 3,"votos": {"A":3000, "B":1900}}
# }
# print(atribui_mandatos({"A":12000, "B":7500, "C":4500, "D":3000}, 7))


def obtem_partidos(eleicoes):
    lista = list(set(x for z in eleicoes for x in eleicoes[z]["votos"]))
    lista.sort()
    return lista

def obtem_resultado_eleicoes(eleicoes):
    resultado = None
    try:
        partidos = obtem_partidos(eleicoes)
        mandatos = []
        res = [[a, 0, 0] for a in partidos]

        if not isinstance(eleicoes, dict) or len(eleicoes) < 1:
            raise ValueError("obtem_resultado_eleicoes: argumento invalido")
        
        for c in eleicoes:
            if type(eleicoes[c]) != dict or not "votos" in eleicoes[c] or not "deputados" in eleicoes[c]:
                raise ValueError("obtem_resultado_eleicoes: argumento invalido")

            if type(eleicoes[c]["deputados"]) != int or type(eleicoes[c]["votos"]) != dict:
                raise ValueError("obtem_resultado_eleicoes: argumento invalido")
            
            if  eleicoes[c]["deputados"] < 1 or len(eleicoes[c]["votos"]) < 1:
                raise ValueError("obtem_resultado_eleicoes: argumento invalido")

            for v in eleicoes[c]["votos"]:
                if type(v) != str or type(eleicoes[c]["votos"][v]) != int or eleicoes[c]["votos"][v] < 0:
                    raise ValueError("obtem_resultado_eleicoes: argumento invalido")
                res[[l[0] for l in res].index(v)][2] += eleicoes[c]["votos"][v]
            
            mandatos += atribui_mandatos(eleicoes[c]["votos"], eleicoes[c]["deputados"])

            if sum(list(eleicoes[c]["votos"].values())) < 1:
                raise ValueError("obtem_resultado_eleicoes: argumento invalido")
        
        for partido in partidos:
            res[[l[0] for l in res].index(partido)][1] += mandatos.count(partido)
        
        res = list(map(tuple, res))
        def compare(e):
            return e[1], e[2]
        res.sort(key=compare, reverse=True)
        return res
    except:
        raise ValueError("obtem_resultado_eleicoes: argumento invalido")

        #mandatos = atribui_mandatos(eleicoes[c]["votos"], eleicoes[c]["deputados"])
        # print(mandatos)
        
        # for partido in partidos:
            # index = [tup[0] for tup in res].index(partido)
            # print(res[index][1])# += mandatos.count(partido)

            #!res += mandatos.count(partido)
            
# MEU
# def obtem_resultado_eleicoes(eleicoes):
#     partidos = obtem_partidos(eleicoes)
#     mandatos = []
#     res = [[a, 0, 0] for a in partidos]

#     if not isinstance(eleicoes, dict) or len(eleicoes) < 1:
#         raise ValueError("obtem_resultado_eleicoes: argumento invalido")
    
#     for c in eleicoes:
#         if type(eleicoes[c]) != dict or not "votos" in eleicoes[c] or not "deputados" in eleicoes[c]:
#             raise ValueError("obtem_resultado_eleicoes: argumento invalido")

#         if type(eleicoes[c]["deputados"]) != int or type(eleicoes[c]["votos"]) != dict:
#             raise ValueError("obtem_resultado_eleicoes: argumento invalido")
        
#         if  eleicoes[c]["deputados"] < 1 or len(eleicoes[c]["votos"]) < 1:
#             raise ValueError("obtem_resultado_eleicoes: argumento invalido")

#         for v in eleicoes[c]["votos"]:
#             if type(v) != str or type(eleicoes[c]["votos"][v]) != int or eleicoes[c]["votos"][v] < 0:
#                 raise ValueError("obtem_resultado_eleicoes: argumento invalido")
#             res[[l[0] for l in res].index(v)][2] += eleicoes[c]["votos"][v]
        
#         mandatos += atribui_mandatos(eleicoes[c]["votos"], eleicoes[c]["deputados"])

#         if sum(list(eleicoes[c]["votos"].values())) < 1:
#             raise ValueError("obtem_resultado_eleicoes: argumento invalido")
    
#     for partido in partidos:
#         res[[l[0] for l in res].index(partido)][1] += mandatos.count(partido)
    
#     res = list(map(tuple, res))
#     def compare(e):
#         return e[1], e[2]
#     print(res)
#     res.sort(key=compare, reverse=True)
#     print(res)
#     return res

# print(obtem_resultado_eleicoes(info))

# SISI
def obtem_resultado_eleicoes(dic): ####rever
    if type(dic) != dict or type(dic) != type({}) or len(dic) < 1:
        raise ValueError("obtem_resultado_eleicoes: argumento invalido")
    for i in dic:
        if type(dic[i]) != dict:
            #raise ValueError("obtem_resultado_eleicoes: argumento invalido")
            raise ValueError("obtem_resultado_eleicoes: argumento invalido")

        #if type(i) != dict:
            #raise ValueError("obtem_resultado_eleicoes: argumento invalido")
        if "deputados" not in dic[i] or "votos" not in dic[i]:  #ver se existe a chave deputados e a chave votos no dict
            raise ValueError("obtem_resultado_eleicoes: argumento invalido")
        if type(dic[i]["deputados"]) != int or type(dic[i]["votos"]) != dict:         
            raise ValueError("obtem_resultado_eleicoes: argumento invalido")
        if len(dic[i]["votos"]) < 1:                            #dicionario de votos nao pode estar vazio
            raise ValueError("obtem_resultado_eleicoes: argumento invalido")
        if len(dic[i]) > 2:                                     #nao haver mais do que duas chaves (apenas deputados e votos)
            raise ValueError("obtem_resultado_eleicoes: argumento invalido") 
        for elemento in dic[i]["votos"]:
            print(dic[i]["votos"][elemento])
            if type(dic[i]["votos"][elemento]) != int or dic[i]["votos"][elemento] <= 0:
                raise ValueError("obtem_resultado_eleicoes: argumento invalido")
        #if dic[i]["votos"] <= 0:                               #nao pode haver partidos com 0 votos ou com votos negativos
            #raise ValueError("obtem_resultado_eleicoes: argumento invalido")
    P = obtem_partidos(dic)                                    #partidos por ordem
    if type(P) != list:
        raise ValueError("obtem_resultado_eleicoes: argumento invalido")
    lista = []
    for i in P:
        lista.append([i,0,0])
    for x in dic:
        y = atribui_mandatos(dic[x]["votos"],dic[x]["deputados"])
        for i in range(len(P)):
            lista[i][1] = lista[i][1] + y.count(P[i])
            if P[i] in dic[x]["votos"]:
                lista[i][2] = lista[i][2] + dic[x]["votos"][P[i]]
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[j][1] < lista[i][1] or (lista[j][1] == lista[i][1] and lista[j][2] < lista[i][2]):
                lista[i] , lista[j] = lista[j] , lista[i]
    for i in range(len(lista)):
        lista[i] = tuple(lista[i])
    return lista
info = {
"Endor": {"deputados": 7,
             "votos": {"A":12000, "B":7500, "C":5250, "D":3000}},
"Hoth":    {"deputados": 6,
             "votos": {"B":11500, "A":9000, "E":5000, "D":1500}},
"Tatooine": {"deputados": 3,
"votos": {"A":3000, "B":1900}}}
print(obtem_resultado_eleicoes(info))

# info = {
# "Endor": {"deputados": 7,
#              "votos": {"A":12000, "B":7500, "C":5250, "D":3000}},
# "Hoth":    {"deputados": 6,
#              "votos": {"B":11500, "A":9000, "E":5000, "D":1500}},
# "Tatooine": {"deputados": 3,
#                 "votos": {"A":3000, "B":1900}}}
# print(obtem_resultado_eleicoes(info))