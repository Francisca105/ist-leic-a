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
            print(tuplo)
            return False
        i += 1
    return True

print(verifica_convergencia( ((1, -0.5), (-1, 2)), (-0.4, 1.9), (0.1001, 1), 0.001))

def retira_zeros_diagonal(tup1, tup2):
    length = len(tup1)
    matriz, const = list(tup1), list(tup2)

    for i in range(length):
        if matriz[i][i] == 0:
            for j in range(length):
                if matriz[i][j] != 0 and matriz[j][i] != 0:
                    print(i, j, tup1[i], tup1[j])
                    matriz[i], matriz[j] = matriz[j], matriz[i]
                    const[i], const[j] = const[j], const[i]
                    print(matriz, const)
                    break

    # for i in range(length):
    #     if tup1[i][i] == 0:
    #         for ii in range(length):
    #             if 

    # poss = [[] for i in range(length)]
    # usados = []

    # for i in range(length):
    #     for ii in range(length):
    #         if tup1[ii][i] != 0:
    #             poss[i].append(ii)

    # for i in range(len(poss)):
    #     if len(poss[i]) == 1:
    #         matriz[i] = tup1[poss[i][0]]
    #         const[i] = tup2[poss[i][0]]
    #         usados.append(poss[i][0])
    #         del poss[i][0]

    # for i in range(len(poss)):
    #     if len(poss[i]) != 0:
    #         for ii in range(len(poss[i])):
    #             if not poss[i][ii] in usados:
    #                 matriz[i] = tup1[poss[i][ii]]
    #                 const[i] = tup2[poss[i][ii]]
    #                 usados.append(poss[i][ii])

    # print('res', matriz, const)
        

    return tuple(matriz), tuple(const)
#print(retira_zeros_diagonal(((0, 1, 1), (1, 0, 0), (0, 1, 0)), (1, 2, 3)))

    # length = len(tup1)
    # matriz = [0] * length
    # constantes = [0] * length

    # usadas = []

    # for i in range(length):
    #     if tup1[i][i] != 0:
    #         usadas.append(i)
    #         matriz[i], constantes[i] = tup1[i], tup2[i]
    #         pass
    #     for ii in range(length):
    #         if tup1[ii][i] != 0:
    #             print('LG', i, ii, tup1[i], tup1[ii])
        
    # return tuple(matriz), tuple(constantes)

    # for i in range(length):
    #     print('mc',matriz, constantes)
    #     if tup1[i][i] != 0 and not i in usadas:
    #         print('a',tup1[i])
    #         usadas.append(i)
    #         break
    #     for ii in range(length):
    #         print(tup1[i], tup1[ii], i, ii, usadas)
    #         if ii in usadas:
    #             print(ii)
    #             break

    #         if tup1[ii][i] != 0:
                 
    #             matriz[i], constantes[i] = tup1[ii], tup2[ii]
    #             usadas.append(ii)

    # while i < length:
    #     for ii in range(length):
    #         print(usadas, ii,i)
    #         if tup1[i][ii] != 0 and not ii in usadas:
    #             usadas.append(ii)
    #             tup1[i] = tup1[ii]
    #             tup2[i] = tup2[ii]
            
    #     i += 1
    # while i < length:
    #     if tup1[i][i] == 0:
    #         for ii in range(length):
    #             print(usadas, ii,i)
    #             if tup1[i][ii] != 0 and not ii in usadas:
    #                 usadas.append(ii)
    #                 tup1[i] = tup1[ii]
    #                 tup2[i] = tup2[ii]
    #                 pass
    #     i += 1

    # _i = 0
    # while _i < length:
    #     for i in range(length):
    #         if tup1[i][i] == 0:
                
    #             print(usadas, _i,i)
    #             if tup1[i][_i] != 0 and i not in usadas:
    #                 usadas.append(i)
    #                 tup1[_i] = tup1[i]
    #                 tup2[_i] = tup2[i]
    #                 # matriz[i] = tup1[_i]
    #                 # linhas[i] = tup2[_i]
    #     _i += 1


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
    for i in  range(len(tup)):
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
            if type(tup1[i][ii]) != float and type(tup1[i][ii]) != int:
                raise ValueError("resolve_sistema: argumentos invalidos")
    
        # if type(tup1[i]) == tuple:
        #     for ii in tup1[i]:
        #         if type(tup1[i][ii]) != int or type(tup1[i][ii]) != float:
        #             raise ValueError("resolve_sistema: argumentos invalidos")
        # raise ValueError("resolve_sistema: argumentos invalidos")

    matriz, const = retira_zeros_diagonal(tup1, tup2)[0], retira_zeros_diagonal(tup1, tup2)[1]

    if not eh_diagonal_dominante(tup1):
        raise ValueError("resolve_sistema: matriz nao diagonal dominante")

    sol = [0 for x in tup2]
    while not verifica_convergencia(matriz, const, sol, real):
        res = sol.copy()
        for l in range(len(matriz)):
            sol[l] = res[l] + (const[l] - produto_interno(matriz[l], res))/matriz[l][l]
    return sol

# resolve_sistema(((2, -1, -1), (2, -9, 7), (-2, 5, -9)), (-8, 8, -6), 1e-20)