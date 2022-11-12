def produto_interno(tup1, tup2):
    soma = 0.0
    for i in range(len(tup1)):
        soma += tup1[i] * tup2[i]
    return soma


A1, c1 = ((1, -0.5), (-1, 2)), (-0.4, 1.9)


def verifica_convergencia(tup1, tup2, tup3, real):
    i = 0
    for tuplo in tup1:
        if abs(produto_interno(tuplo, tup3) - tup2[i]) >= real:
            return False
        i += 1
    return True


def retira_zeros_diagonal(tup1, tup2):
    length = len(tup1)
    matriz = list(tup1)
    linhas = list(tup2)

    for i in range(length):
        if tup1[i][i] == 0:
            _i = 0
            while _i < length:

                if tup1[_i][i] != 0 and tup1[i][_i] != 0:
                    matriz[i] = tup1[_i]
                    linhas[i] = tup2[_i]
                _i += 1
        # else:
        #     matriz[i] = tup1[i]
        #     linhas[i] = tup2[i]

    return tuple(matriz), tuple(linhas)
#{{"A"}: "A"}
d = {}
d['True'] += 1
    # for i in range(len(tup1)):
    #     if tup1[i][i] == 0:
    #         _i = 0
    #         while _i < len(tup1):
    #             print(i, _i, matriz, linhas)
    #             if linhas[i] != 0:
    #                 _i+=1
    #                 continue
    #             # if _i+1 in linhas:
    #             #     continue
    #             if tup1[_i][i] == 0:
    #                 matriz[i] = tup1[_i]
    #                 linhas[i] = tup2[_i]

    #             else:
    #                 matriz[i] = tup1[i]
    #                 linhas[i] = tup2[i]

    #             _i+=1
    # print(matriz, linhas)

    # matriz = [i for i in range(len(tup1))]
    # linhas = [i+1 for i in range(len(tup2))]
    # s_z = []
    # for i in range(len(tup1)):
    #     if tup1[i][i] != 0:
    #         matriz[i] = tup1[i]
    #         linhas[i] = tup2[i]
    #         continue
    #     s_z.append((tup2[i], tup1[i]))

    # for i in range(len(s_z)):
    #     _i = 0
    #     while _i+1 < len(s_z):
    #         print(linhas)
    #         if s_z[_i+1][1][i] == 0:
    #             matriz[i] = s_z[_i+1][1]
    #             linhas[i] = s_z[i][0]
    #             del s_z[_i+1]
    #         _i += 1
    #     if len(s_z) == 1:
    #         matriz[len(matriz) - 1] = s_z[0][1]
    #         print(matriz, linhas, s_z[0][0])
    #         linhas[len(matriz) - 1] = s_z[0][0]
    #         del s_z[0]

    # return list(matriz), list(linhas) # 2 3 1

    # print(matriz, linhas)


def eh_diagonal_dominante(tup):
    for i in range(len(tup)):
        soma = 0
        for j in range(len(tup[i])):
            if j != i:
                soma += abs(tup[i][j])
        if abs(tup[i][i]) < soma:
            return False

    return True


def resolve_sistema(tup1, tup2, real):
    if type(tup1) != tuple or type(tup2) != tuple or type(real) != float or\
        len(tup1) == 0 or len(tup2) == 0 or\
            len(tup1) != len(tup2) or\
            real <= 0:
        raise ValueError("resolve_sistema: argumentos invalidos")

    for e in tup2:
        if type(e) != float and type(e) != int:
            raise ValueError("resolve_sistema: argumentos invalidos")

    for i in range(len(tup1)):
        if type(tup1[i]) != tuple or\
                len(tup1) != len(tup1[i]):
            raise ValueError("resolve_sistema: argumentos invalidos")

        for ii in range(len(tup1[i])):
            if not type(tup1[i][ii]) in [int, float]:
                raise ValueError("resolve_sistema: argumentos invalidos")

    tup1, tup2 = retira_zeros_diagonal(
        tup1, tup2)[0], retira_zeros_diagonal(tup1, tup2)[1]
    if not eh_diagonal_dominante(tup1):
        # if not eh_diagonal_dominante(retira_zeros_diagonal(tup1, tup2)):
        raise ValueError("resolve_sistema: matriz nao diagonal dominante")

        # if type(tup1[i]) == tuple:
        #     for ii in tup1[i]:
        #         if type(tup1[i][ii]) != int or type(tup1[i][ii]) != float:
        #             raise ValueError("resolve_sistema: argumentos invalidos")
        # raise ValueError("resolve_sistema: argumentos invalidos")


A4, c4 = ((2, -1, -1), (2, -9, 7), (-2, 5, -9)), (-8, 8, -6)
print(resolve_sistema(A4, c4, 1e-20))
