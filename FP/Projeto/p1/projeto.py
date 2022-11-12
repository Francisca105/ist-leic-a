# # 1 # #

# 1.2.1

def limpa_texto(t):
    '''
    Esta funcao recebe uma cadeia de carateres e devolve a cadeia de carateres limpa (sem caracteres brancos).
    '''
    return  " ".join(t.split()) # Separa o texto e junta-o numa nova string removendo caracteres branco e de escape

# 1.2.2

def corta_texto(string, int):
    '''
    Esta funcao recebe uma cadeia de caracteres e um numero inteiro a que correspondem, respetivamente, a um texto limpo (podendo recorrer a funcao anterior) e a largura da coluna.
    Ao separar o texto em 2, esta nao corta nenhuma palavra, ou seja, as palavras ficam todas completas e este tera no maximo um comprimento igual a largura fornecida. A segunda cadeira corresponde ao resto.
    '''
    tuplo = string.split() # Separar a cadeia em palavras
    length = 0 # Variavel auxiliar para o tamanho da primeira cadeia de forma a nao exceder o tamanho suposto
    res = ["", ""] # Resultado da funcao
    extra = False # Variavel auxiliar que ira determinar se este ja chegou ao valor maximo da primeira cadeia

    for e in tuplo:
        lenE = len(e)
        if (length + lenE) <= int and not extra: # Verifica se nao excede o tamanho e com recurso a variavel extra verifica se pode adicionar
            length += lenE +1 # Adiciona a length o tamanho da palavra +1 (do espaco entre as palavras)
            res[0] += f"{e} " # Acrescenta ao primeiro texto a palavra +1 espaco
        else:
            extra = True # Para nao executar o if anterior quando ja passou do tamanho pela primeira vez
            res[1] += f"{e} " # Adiciona ao segundo texto a palavra + espaco
    resultado = limpa_texto(res[0]), limpa_texto(res[1]) # Se tiver um espaco a mais no final dos textos este sera limpo

    return tuple(resultado) # Passar a lista a tuplo que e o formato pedido

# 1.2.3

def insere_espacos(string, int):
    '''
    Esta funcao recebe uma cadeia de carateres e um inteiro positivo correspondentes a um
    texto limpo e uma largura de coluna respetivamente, e no caso da cadeia de entrada
    conter duas ou mais palavras devolve uma cadeia de carateres de comprimento igual
    a largura da coluna formada pela cadeia original com espacos entre palavras.
    Caso contrario, devolve a cadeia de comprimento igual a largura da coluna
    formada pela cadeia original seguida de espacos.
    '''
    res = ""
    split = string.split() # Separa a cadeia em palavras
    palavras = len(split) # Variavel auxiliar para o tamanho do split
    espacos = int - len(string.replace(" ","")) # Ao numero fornecido, int, retira o tamanho da cadeia sem contar com espacos
    spaces = [0] * (palavras-1) # Cria uma lista com o tamanho de espacos original

    if palavras == 1: # Se for so uma palavra acrescenta os espacos diretamente
        res = split[0] + " "*espacos 
        return res
    
    while espacos > 0: 
        for i in range(len(spaces)):
            if espacos > 0:
                espacos -= 1 # Tira um espaco a variavel auxiliar
                spaces[i] += 1 # Acrescenta um espaco ao sitio correspondente

    i = 0

    for p in split:
        if (i+1) == len(split): 
            res += p # Nao acrescenta um espaco pois seria a ultima palavra
        else:
            res += p+" "*spaces[i] # Acrescenta os espacos pretendidos de acordo com o que foi definido dentro do while
        i+=1
    return res

# 1.2.4

def justifica_texto(string, inteiro):
    '''
    Esta funcao recebe uma cadeia de caracteres e um numero positivo correspondentes a um texto e uma largura de coluna.
    Este ira devolver um tuplo com textos justificados, ou seja, com comprimento IGUAL a largura da coluna inserindo espacos
    entre palavras ou no fim da frase (caso esta seja a ultima do tuplo).
    '''
    if not isinstance(string, str) or not isinstance(inteiro, int) or inteiro <= 0 or len(string) == 0: # Verifica o tipo dos argumentos fornecidos se estao de acordo com o pretendido
        raise ValueError("justifica_texto: argumentos invalidos")
    for e in string.split():
        if len(e) > inteiro:
            raise ValueError("justifica_texto: argumentos invalidos")

    string = limpa_texto(string) # Limpa o texto para podermos comecar a trabalhar
    res = () # Resultado
    cortado = corta_texto(string, inteiro) # Corta o texto da primeira parte do texto
    while cortado[1] != "":
        res += (insere_espacos(cortado[0], inteiro),) # Adiciona ao resultado a primeira parte do resultado da funcao auxiliar que tem o formato pretendido
        cortado = corta_texto(cortado[1],inteiro) # Continua o processo
    res += (cortado[0] + " "*(inteiro - len(cortado[0])), ) # Acrescenta o ultimo ao texto
    return res

# # 2 # #

# 2.2.1

def calcula_quocientes(circulo, n):
    '''
    Esta funcao recebe um dicionario com os votos apurados num circulo (com pelo menos
    um partido) e um inteiro positivo representando o numero de deputados e devolve o
    dicionario com as mesmas chaves do dicionario argumento (correspondente a partidos)
    contendo a lista (de comprimento igual ao numero de deputados) com os quocientes
    calculados com o metodo de Hondt ordenados em ordem decrescente. Esta funcao nao
    deve de alterar o dicionario que e passado como argumento de entrada.
    '''

    i = 1
    resultado = {p: [] for p in circulo} # p representa o nome do partido
    while n >= i: # Enquanto nao chegar ao numero de deputados continua
        for p in circulo: # p representa o nome do partido
            resultado[p].append(circulo[p] / i)
        i+=1
    return resultado

# 2.2.2

def atribui_mandatos(circulo, n):
    '''
    Esta funcao recebe um dicionario com os votos apurados num circulo e um inteiro representando o numero de deputados,
    e devolve a lista ordenada de tamanho igual ao numero de deputados contendo as cadeias de carateres dos partidos
    que obtiveram cada mandato.
    '''
    valores = calcula_quocientes(circulo, n)
    res = []
    while n > 0:
        maximo = max(valores, key=valores.get) # Procura o valor maximo de "valores" e esse sera o pretendido para o mandato
        value = maximo # Valor a acrescentar no resultado final
        for p in valores:
            if p != maximo and  valores[p][0] == valores[maximo][0] and res.count(maximo) > res.count(p): # Verifica se e o valor maximo e se tiver mais algum partido com igual quociente, este e atribuido ao que tiver menos listas votadas
                value = p

        res.append(value)
        del valores[value][0] # Retira o valor para este nao ser mais avaliado
        n -= 1 # O mandato foi atribuido entao retira-o
    return res

# 2.2.3

def obtem_partidos(eleicoes):
    '''
    Esta funcao recebe um dicionario com a informacao sobre as eleicoes num territorio
    com varios circulos eleitorais como descrito, e devolve a lista por ordem alfabetica com
    o nome de todos os partidos que participaram nas eleicoes.
    '''
    lista = list(set(x for z in eleicoes for x in eleicoes[z]["votos"])) # Com recurso ao set, que retira logo entradas duplicadas, lista todos os partidos
    lista.sort() # Organiza-os por ordem alfabetica
    return lista

# 2.2.4

def obtem_resultado_eleicoes(eleicoes):
    '''
    Esta funcao recebe um dicionario com as informacoes das eleicoes num territorio com diversos circulos eleitorais
    e devolve a lista ordenada de comprimento igual ao numero total de partidos com os resultados das eleicoes
    '''
    try: # Caso de erro para levantar ValueError
        partidos = obtem_partidos(eleicoes) # Lista os partidos existentes
        mandatos = []
        res = [[a, 0, 0] for a in partidos] # Torna a lista numa lista organizada com o resultado obtido sendo os 2 0s valores a alterar ao longo da funcao

        if not isinstance(eleicoes, dict) or len(eleicoes) < 1: # Verifica o tipo dos argumentos se e o pretendido e se tem pelo menos um partido
            raise ValueError("obtem_resultado_eleicoes: argumento invalido")
        
        for c in eleicoes:
            if type(eleicoes[c]) != dict or len(eleicoes[c]) != 2 or not "votos" in eleicoes[c] or not "deputados" in eleicoes[c]: # Verifica o tipo e se so existe a chave deputados e votos dentro do dicionario
                raise ValueError("obtem_resultado_eleicoes: argumento invalido")

            if type(eleicoes[c]["deputados"]) != int or type(eleicoes[c]["votos"]) != dict: # Verifca o tipo a ver se e o pretendido
                raise ValueError("obtem_resultado_eleicoes: argumento invalido")
            
            if  eleicoes[c]["deputados"] < 1 or len(eleicoes[c]["votos"]) < 1: # Verifica o numero de deputados e votos
                raise ValueError("obtem_resultado_eleicoes: argumento invalido")

            for v in eleicoes[c]["votos"]:
                if len(v) == 0 or type(v) != str or type(eleicoes[c]["votos"][v]) != int or eleicoes[c]["votos"][v] < 0: # Verifica os tipos e se algum partido tem votos negativos
                    raise ValueError("obtem_resultado_eleicoes: argumento invalido")
                res[[l[0] for l in res].index(v)][2] += eleicoes[c]["votos"][v] # Aumenta o numero de votos no resultado
            
            mandatos += atribui_mandatos(eleicoes[c]["votos"], eleicoes[c]["deputados"]) 

            if sum(list(eleicoes[c]["votos"].values())) < 1: # Verifica se tem pelo menos um voto nos partidos de uma entrada
                raise ValueError("obtem_resultado_eleicoes: argumento invalido")
        
        for partido in partidos:
            res[[l[0] for l in res].index(partido)][1] += mandatos.count(partido) # Acrescenta ao resultado o numero de mandatos do partido
        
        res = list(map(tuple, res)) # Muda o tipo lista dentro de lista para tuplo dentro de lista
        def compare(e):
            return e[1], e[2]
        res.sort(key=compare, reverse=True) # Ordena por ordem decrescente
        return res
    except:
        raise ValueError("obtem_resultado_eleicoes: argumento invalido")

# # 3 # #

# 3.2.1

def produto_interno(tup1, tup2):
    '''
    Esta funcao recebe dois tuplos de numeros com a mesma dimensao representando dois vetores e retorna o resultado do produto interno desses 2 vetores
    '''
    soma = 0.0
    for i in range(len(tup1)):
        soma += tup1[i] * tup2[i] # Acrescenta a soma o produto de duas entradas da mesma linha e coluna
    return soma

# 3.2.2

def verifica_convergencia(tup1, tup2, tup3, real):
    '''
    Esta funcao recebe tres tuplos de igual dimensao e um valor real positivo. O primeiro
    tuplo e constituido por um conjunto de tuplos cada um representando uma linha da
    matriz quadrada A, e os outros dois tuplos de entrada contem valores representando
    respetivamente o vetor de constantes e a solucao atual. O valor real de entrada
    indica a precisao pretendida. Este retorna True no caso do valor abosulto for inferior a precisa e False caso contrario.
    '''
    for i in range(len(tup1)):
        if abs(produto_interno(tup1[i], tup3) - tup2[i]) >= real: # Faz a diferente entre o produto interno e a constante e verifica se e superior ou igual ao real
            return False
    return True

# 3.2.3

def retira_zeros_diagonal(tup1, tup2):
    '''
    Esta funcao recebe um tuplo de tuplos representando uma matriz e um vetor de constantes.
    Esta retorna uma nova matriz em que em todas as linhas que tenha algum 0 na diagonal troquem pela primeira que tenha um numero diferente de 0.
    '''
    length = len(tup1) # Tamanho da matriz
    matriz, const = list(tup1), list(tup2) # Copia os tuplos para listas

    for i in range(length): # Para cada linha da matriz
        if matriz[i][i] == 0: # Verifica se a diagonal tem valor nulo
            for j in range(length):
                if matriz[i][j] != 0 and matriz[j][i] != 0: # Verifica se tem alguma outra linha cujo a entrada da diagonal que estamos a verificar nao e zero e se a respetiva entrada da diagonal na linha atual nao e zero de forma a conseguirmos trocar
                    matriz[i], matriz[j] = matriz[j], matriz[i] # Troca as linhas
                    const[i], const[j] = const[j], const[i] # Troca as constantes
                    break
    return tuple(matriz), tuple(const) # Retorna o valor como tuplos

# 3.2.4

def eh_diagonal_dominante(tup):
    '''
    Esta funcao recebe um tuplo de tuplos representando uma matriz quadrada no mesmo
    formato das funcoes anteriores. Esta verifica se a diagonal da matriz e dominante ou nao.
    '''
    for i in  range(len(tup)):
        soma = 0
        for j in range(len(tup[i])):
            if j != i:
                soma += abs(tup[i][j]) # Acrescenta a soma dos valores na linha todos os elementos que nao pertencem a diagonal
        if abs(tup[i][i]) < soma: # Se o modulo do valor da entrada da diagonal de uma linha for inferior a soma retorna False
            return False
    return True # No caso de ja nao ter retornado False, retorna True

# 3.2.5

def resolve_sistema(tup1, tup2, real):
    '''
    Esta funcao recebe um tuplo de tuplos representando uma matriz quadrada correspondente
    aos coeficientes das equacoes do sistema, um tuplo de numeros representando o vetor das
    constantes, e um valor real positivo correspondente a precisao pretendida para a solucao.
    Esta retorna um tuplo com a solucao do sistema aplicando o metodo de Jacobi.
    '''
    # 
    # Verifica os argumentos
    #

    if type(tup1) != tuple or type(tup2) != tuple or type(real) != float or\
            len(tup1) == 0 or len(tup2) == 0 or\
                len(tup1) != len(tup2) or\
                    real <= 0:
        raise ValueError("resolve_sistema: argumentos invalidos")
    # No primeiro verifica o tipo dos argumentos, se o tamanho das constantes ou da matriz e zero, se tem igual numero de constantes e de linhas da matriz e se a precisao e superior a zero

    for e in tup2:
        if type(e) != float and type(e) != int: # Verifica o tipo dos numeros dentro das constantes
            raise ValueError("resolve_sistema: argumentos invalidos")

    for i in range(len(tup1)):
        if type(tup1[i]) != tuple or\
            len(tup1) != len(tup1[i]): # Verifica o tipo da linha, que e tuplo e se a matriz e quadrada
            raise ValueError("resolve_sistema: argumentos invalidos")

        for ii in range(len(tup1[i])):
            if type(tup1[i][ii]) != float and type(tup1[i][ii]) != int: # Verifica se para cada elemento da linha este corresponde a um inteiro ou um float
                raise ValueError("resolve_sistema: argumentos invalidos")

    matriz, const = retira_zeros_diagonal(tup1, tup2)[0], retira_zeros_diagonal(tup1, tup2)[1] # Retira os zeros da diagonal para poder aplicar o metodo

    if not eh_diagonal_dominante(tup1):
        raise ValueError("resolve_sistema: matriz nao diagonal dominante") # Se nao for diagonal dominante nao pode usar o metodo

    sol = [0 for x in tup2] # Cria uma lista com um numero de 0s igual ao numero de constantes
    while not verifica_convergencia(matriz, const, sol, real): # Enquanto nao convergir...
        res = sol.copy() # Faz uma copia da solucao anterior
        for l in range(len(matriz)): # Altera para cada linha ->
            sol[l] = res[l] + (const[l] - produto_interno(matriz[l], res))/matriz[l][l] # A solucao usando a formula

    return sol # Retorna a solucao