#
#                        Projeto 2 - Minas - FP 
#

# 2.1.1


def cria_gerador(b, s):
    """
    Esta função cria um gerador (usando dois numeros para bits e seed/estado
    inicial) e verifica a validade dos argumentos fornecidos.
    --------------------------
    {int x int} -> {"gerador"}
    """

    if not isinstance(b, int) or (b != 32 and b != 64) \
            or not isinstance(s, int) or not 0 < s < 2**b:
        raise ValueError("cria_gerador: argumentos invalidos")

    # Gerador no formato de um dicionario, sendo b bits e s a seed.
    return {"b": b, "s": s}


def cria_copia_gerador(g):
    """
    Esta função cria a copia de um gerador.
    --------------------------
    {"gerador"} -> {"gerador"}
    """

    return g.copy()


def obtem_estado(g):
    """
    Esta função retorna o estado ("seed") de um gerador.
    --------------------
    {"gerador"} -> {int}
    """
    return g["s"]


def define_estado(g, s):
    """
    Esta função atualiza o estado ("seed") de um gerador e retorna-o.
    --------------------------
    {"gerador" x int} -> {int}
    """

    g["s"] = s
    return s


def atualiza_estado(g):
    """
    Esta função atualiza o estado ("seed") de um gerador, de acordo com o algoritmo
    xorshift de geração de números pseudoaleatórios, e devolve-o.
    --------------------
    {"gerador"} -> {int}
    """

    s = obtem_estado(g)

    lista = (13, 17, 5) if g["b"] == 32 else (13, 7, 17)
    hex = 0xFFFFFFFF if g["b"] == 32 else 0xFFFFFFFFFFFFFFFF
    for i in range(3):  # Executa as operações de xorshift conforme seja de 32 ou 64 bits
        n = lista[i]
        if i % 2 == 0:
            s ^= (s << n) & hex
        else:
            s ^= (s >> n) & hex
    define_estado(g, s)  # Define o estado do gerador com a nova seed (s)

    return s


def eh_gerador(g):
    """
    Esta função retorna se um argumento é um gerador.
    ---------------------
    {universal} -> {bool}
    """

    return isinstance(g, dict) and len(g) == 2 and "b" in g and "s" in g \
        and type(obtem_estado(g)) == type(g["b"]) == int


def geradores_iguais(g1, g2):
    """
    Esta função verifica se dois geradores são iguais.
    ---------------------------------
    {"gerador" x "gerador"} -> {bool}
    """

    return g1 == g2


def gerador_para_str(g):
    """
    Esta função devolve uma cadeia de carateres que representa um gerador.
    --------------------
    {"gerador"} -> {str}
    """

    return f'xorshift{g["b"]}(s={obtem_estado(g)})'


def gera_numero_aleatorio(g, n):
    """
    Esta função atualiza o estado do gerador e devolve um número aleatório no
    intervalo de [1,n] obtido a partir do novo estado da seed do gerador.
    --------------------------
    {"gerador" x int} -> {int}
    """

    atualiza_estado(g)
    return 1 + obtem_estado(g) % n


def gera_carater_aleatorio(g, c):
    """
    Esta função atualiza o estado do gerador e devolve um caracter aleatório da
    lista de letras de A até essa letra, obtido a partir do novo estado da seed do gerador.
    --------------------------
    {"gerador" x str} -> {str}
    """

    atualiza_estado(g)
    minimo = ord('A')
    maximo = ord(c)
    letras = [chr(n) for n in range(minimo, maximo + 1)]
    n = obtem_estado(g) % len(letras)

    return letras[n]


# 2.1.2


def cria_coordenada(col, lin):
    """
    Esta função cria uma coordenada (usando uma letra e um numero para a coluna e
    a linha, respetivamente) e verifica a validade dos argumentos fornecidos.
    --------------------------
    {str x int} -> {"coordenada"}
    """

    if not isinstance(lin, int) or not isinstance(col, str) \
            or not 99 >= lin >= 1 or len(col) > 1 or not 90 >= ord(col) >= 65:
        raise ValueError("cria_coordenada: argumentos invalidos")
    # Coordenadas do tipo de dicionario em que a chave col representa a coluna e lin a linha.
    return {"col": col, "lin": lin}


def obtem_coluna(coordenada):
    """
    Esta função devolve a coluna de uma coordenada.
    --------------------------
    {"coordenada"} -> {str}
    """

    return coordenada["col"]


def obtem_linha(coordenada):
    """
    Esta função devolve a linha de uma coordenada.
    --------------------------
    {"coordenada"} -> {int}
    """

    return coordenada["lin"]


def eh_coordenada(arg):
    """
    Esta função retorna se um argumento é uma coordenada.
    ---------------------
    {universal} -> {bool}
    """

    return isinstance(arg, dict) and len(arg) == 2 and "col" in arg and "lin" in arg \
        and isinstance(obtem_coluna(arg), str) and isinstance(obtem_linha(arg), int) \
        and 99 >= obtem_linha(arg) >= 1 and ord("A") <= ord(obtem_coluna(arg)) <= ord("Z")


def coordenadas_iguais(c1, c2):
    """
    Esta função verifica se duas coordenadas são iguais.
    ---------------------------------------
    {"coordenada" x "coordenada"} -> {bool}
    """

    return obtem_coluna(c1) == obtem_coluna(c2) and obtem_linha(c1) == obtem_linha(c2)


def coordenada_para_str(c):
    """
    Esta função retorna uma cadeia de caracteres que representam uma coordenada.
    -----------------------
    {"coordenada"} -> {str}
    """

    numero = obtem_linha(c) if obtem_linha(c) >= 10 else f'0{obtem_linha(c)}'
    return f"{obtem_coluna(c)}{numero}"


def str_para_coordenada(c):
    """
    Esta função usa uma cadeia de caracteres que representam uma coordenada e transforma numa coordenada.
    -----------------------
    {str} -> {"coordenada"}
    """

    return cria_coordenada(c[:1], int(c[1:]))


def obtem_coordenadas_vizinhas(c):
    """
    Esta função recebe uma coordenada e devolve as coordenadas vizinhas, começando
    pela coordenada da diagonal superior-esqueda e seguinte o sentido horário.
    -------------------------
    {"coordenada"} -> {tuple}
    """

    coluna, linha = ord(obtem_coluna(c)), obtem_linha(c)
    n = 0
    coords = []
    while n <= 8:
        n += 1
        l, c = 0, 0

        # Visualmente, o que o loop vai verificando é:
        # 1 2 3
        # 8 c 4
        # 7 6 5

        if n in (1, 7, 8) and coluna - 1 >= ord('A'):  # Se for da coluna anterior, caso exista
            c = coluna - 1
        if n in (2, 6):  # Mesma coluna
            c = coluna
        if n in (3, 4, 5) and coluna + 1 <= ord('Z'):  # Se for da coluna seguinte, caso exista
            c = coluna + 1
        if n in (1, 2, 3) and linha - 1 > 0:  # Se for da linha anterior, caso exista
            l = linha - 1
        if n in (4, 8):  # Da mesma linha
            l = linha
        if n in (5, 6, 7) and linha + 1 < 100:  # Se for da linha seguinte, caso existe
            l = linha + 1
        if c == 0 or l == 0:  # Se um dos valores não foi alterado então continua
            continue
        coords.append(cria_coordenada(chr(c), l))

    return tuple(coords)


def obtem_coordenada_aleatoria(c, g):
    """
    Esta função recebe uma coordenada e devolve uma coordenada aleatoria em que a
    coordenada fornecida define o tamanho máximo da coluna e da linha.
    --------------------------------------------
    {"coordenada" x "gerador"} -> {"coordenada"}
    """

    coluna = gera_carater_aleatorio(g, obtem_coluna(c))
    linha = gera_numero_aleatorio(g, obtem_linha(c))
    return cria_coordenada(coluna, linha)


# 2.1.3


def cria_parcela():
    """
    Esta função devolve uma parcela tapada sem mina escondida.
    -----------------
    {} -> {"parcela"}
    """

    # Parcela no formato de dicionário com as propriedades necessárias
    return {"estado": "tapada", "marcada": False, "mina": False}


def cria_copia_parcela(p):
    """
    Esta função devolve uma cópia de uma parcela.
    --------------------------
    {"parcela"} -> {"parcela"}
    """

    return p.copy()

def marca_parcela(p):
    """
    Esta função modifica destrutivamente a parcela p modificando o seu estado para marcada.
    --------------------------
    {"parcela"} -> {"parcela"}
    """

    p["marcada"] = True
    return p


def desmarca_parcela(p):
    """
    Esta função modifica destrutivamente a parcela p modificando o seu estado para não marcada.
    --------------------------
    {"parcela"} -> {"parcela"}
    """

    p["estado"] = "tapada"
    p["marcada"] = False
    return p

def limpa_parcela(p):
    """
    Esta função modifica destrutivamente a parcela p modificando o seu estado para limpa.
    --------------------------
    {"parcela"} -> {"parcela"}
    """
    if eh_parcela_marcada(p):
        p["marcada"] = False
    p["estado"] = "limpa"
    return p

def esconde_mina(p):
    """
    Esta função modifica destrutivamente a parcela p modificando o seu estado para mina escondida.
    --------------------------
    {"parcela"} -> {"parcela"}
    """

    p["mina"] = True
    return p


def eh_parcela(p):
    """
    Esta função recebe um argumento e verifica se é uma parcela.
    ---------------------
    {universal} -> {bool}
    """

    return type(p) == dict and len(p) == 3 and "mina" in p and "estado" in p and "marcada" in p \
        and type(p["mina"]) == bool and p["estado"] in ("tapada", "limpa") and type(p["marcada"]) == bool


def eh_parcela_marcada(p):
    """
    Esta função verifica se a parcela é marcada.
    ---------------------
    {"parcela"} -> {bool}
    """

    return p["marcada"]


def eh_parcela_tapada(p):
    """
    Esta função verifica se a parcela é tapada.
    ---------------------
    {"parcela"} -> {bool}
    """

    return not eh_parcela_marcada(p) and p["estado"] == "tapada"


def eh_parcela_limpa(p):
    """
    Esta função verifica se a parcela é limpa.
    ---------------------
    {"parcela"} -> {bool}
    """

    return not eh_parcela_marcada(p) and p["estado"] == "limpa"


def eh_parcela_minada(p):
    """
    Esta função verifica se a parcela é minada.
    ---------------------
    {"parcela"} -> {bool}
    """

    return p["mina"]


def parcelas_iguais(p1, p2):
    """
    Esta função verifica se duas parcelas são iguais.
    ---------------------------------
    {"parcela" x "parcela"} -> {bool}
    """

    return p1 == p2


def parcela_para_str(p):
    """
    Esta função devolve a cadeia de caracteres que representa a parcela em funcao do seu estado:
    parcelas tapadas (#), parcelas marcadas (@), parcelas limpas sem mina (?) e parcelas limpas com mina (X).
    --------------------
    {"parcela"} -> {str}
    """

    if p["estado"] == "limpa" and p["mina"]:
        return "X"
    elif p["marcada"]:
        return "@"
    elif p["estado"] == "tapada":
        return "#"
    elif p["estado"] == "limpa" and not p["mina"]:
        return "?"


def alterna_bandeira(p):
    """
    Esta função recebe uma parcela p e modifica-a destrutivamente (desmarca se estiver marcada e marca
    se estiver tapada, devolvendo True. Em qualquer outro caso, nao modifica a parcela e devolve False.)
    ---------------------
    {"parcela"} -> {bool}
    """

    if eh_parcela_marcada(p):
        desmarca_parcela(p)
        return True
    elif eh_parcela_tapada(p):
        marca_parcela(p)
        return True
    else:
        return False


# 2.1.4


def cria_campo(col, lin):
    """
    Esta função cria um campo (usando uma letra e um numero para o tamanho maximo de colunas
    e de linhas, respetivamente) e verifica a validade dos argumentos fornecidos.
    ------------------------
    {str x int} -> {"campo"}
    """

    if not isinstance(lin, int) or not isinstance(col, str) or not 99 >= lin >= 1 \
            or len(col) > 1 or not ord("Z") >= ord(col) >= ord("A"):
        raise ValueError("cria_campo: argumentos invalidos")

    d = {"col": col, "lin": lin, "coords": {}}  # Dicionário base

    for i in range(1, lin+1):
        for ii in range(ord('A'), ord(col)+1):
            # Vai criando as parcelas para X coordenada
            d["coords"][coordenada_para_str(
                cria_coordenada(chr(ii), i))] = cria_parcela()
    return d

def cria_copia_campo(m):
    """
    Esta função recebe um campo e retorna a sua cópia.
    ----------------------
    {"campo"} -> {"campo"}
    """
    # loop A - col
    # 
    copy = cria_campo(m["col"], m["lin"])

    for c in m["coords"].items():
        try:
            coord, parcela = c
            if not eh_parcela_tapada(parcela) or eh_parcela_marcada(parcela) or eh_parcela_minada(parcela):
                copy["coords"][coordenada_para_str(str_para_coordenada(coord))] = cria_copia_parcela(parcela)
        except:
            continue

    return copy

def obtem_ultima_coluna(c):
    """
    Esta função recebe um campo e retorna a letra da última coluna.
    ------------------
    {"campo"} -> {str}
    """

    return c["col"]


def obtem_ultima_linha(c):
    """
    Esta função recebe um campo e retorna o numero da última linha.
    ------------------
    {"campo"} -> {int}
    """

    return c["lin"]


def obtem_parcela(campo, coord):
    """
    Esta função retorna a parcela de uma coordenada.
    ---------------------------------------
    {"campo" x "coordenada"} -> {"parcela"}
    """

    coord = coordenada_para_str(coord)
    return campo["coords"][coord]


def obtem_coordenadas(c, s):
    """
    Esta função devolve o tuplo formado pelas coordenadas ordenadas em ordem ascendente da esquerda para a direita e de cima a baixo das parcelas dependendo do valor de s.
    --------------------------
    {"campo" x str} -> {tuple}
    """

    coordenadas = c["coords"]
    lista = []
    for cc in coordenadas:
        parcela = coordenadas[cc]
        # "Filtra" as coordenadas de forma a retornar aquelas do valor s que queremos.
        if (s == "limpas" and eh_parcela_limpa(parcela)) or \
            (s == "marcadas" and eh_parcela_marcada(parcela)) or \
                (s == "minadas" and eh_parcela_minada(parcela)) or \
                (s == "tapadas" and eh_parcela_tapada(parcela)):

            lista.append(str_para_coordenada(cc))

    return tuple(lista)


def obtem_numero_minas_vizinhas(campo, coord):
    """
    Esta função devolve o numero de parcelas vizinhas da parcela na coordenada
    "coord" que escondem uma mina.
    ---------------------------------
    {"campo" x "coordenada"} -> {int}
    """
    vizinhas = obtem_coordenadas_vizinhas(coord)
    minadas = obtem_coordenadas(campo, "minadas")
    # Retorna o tamanho da lista das coordenadas que são vizinhas e minadas
    return len(tuple(filter(lambda x: x in vizinhas, minadas)))


def eh_campo(c):
    """
    Esta função recebe um argumento e verifica se é um campo.
    ---------------------
    {universal} -> {bool}
    """

    if not (isinstance(c, dict) and len(c) == 3 and "col" in c and "lin" in c and "coords" in c
            and isinstance(c["coords"], dict) and isinstance(obtem_ultima_linha(c), int)
            and isinstance(obtem_ultima_coluna(c), str)
            and ord("Z") >= ord(obtem_ultima_coluna(c)) >= ord("A")
            and 99 >= obtem_ultima_linha(c) > 0):
        return False

    for coord,p in c["coords"].items():
        if not eh_parcela(p):
            return False
        try:
            str_para_coordenada(coord)
        except:
            return False

    return True


def eh_coordenada_do_campo(campo, coord):
    """
    Esta função recebe um campo e uma coordenada verifica se pertence ao campo.
    ---------------------
    {"campo" x "coordenada"} -> {bool}
    """

    coluna, linha = obtem_coluna(coord), obtem_linha(coord)
    max_c, max_l = obtem_ultima_coluna(campo), obtem_ultima_linha(campo)
    return ord("A") <= ord(coluna) <= ord(max_c) and 1 <= linha <= max_l


def campos_iguais(c1, c2):
    """
    Esta função recebe dois campos e verifica se são iguais.
    ---------------------
    {"campo" x "campo"} -> {bool}
    """
    if not eh_campo(c1) or not eh_campo(c2):
        return False

    if obtem_ultima_coluna(c1) != obtem_ultima_coluna(c2) or obtem_ultima_linha(c1) != obtem_ultima_linha(c2):
        return False
    
    c1, c2 = c1["coords"].items(), c2["coords"].items()

    for i in range(len(c1)):
        _c1, _c2 = c1[i], c2[i]
        if  _c1[0] != _c2[0] or not parcelas_iguais(_c1[1], _c1[1]): 
            return False
        


def campo_para_str(campo):
    """
    Esta função devolve uma cadeia de caracteres que representa o campo de minas.
    ------------------
    {"campo"} -> {str}
    """

    # Lista com o numero de linhas + 3 (para listar as colunas, e outras duas para as linhas da tabela)
    linhas = [""] * (obtem_ultima_linha(campo) + 3)
    coords = list(campo["coords"].items())
    col = obtem_ultima_coluna(campo)

    for i in range(ord("A"), ord(col) + 1):  # Formatação da tabela
        if i == ord("A"):
            linhas[0] += "   "
            linhas[1] += "  +"

        linhas[1] += "-"
        linhas[0] += f"{chr(i)}"

        if i == ord(col):
            linhas[1] += "+"

    linhas[-1] = linhas[1]  # Linhas da tabela

    for i in range(1, obtem_ultima_linha(campo) + 1):
        # Se o número for inferior a 10 acrescenta um 0 antes
        linhas[i+1] += f"{i}|" if i >= 10 else f"0{i}|"
        num = (ord(col) - ord("A")) + 1
        # Vê os elementos de uma linha do campo, sendo e -> (coordenada em string, parcela)
        for e in coords[(i-1) * num: i * num]:
            coord, parcela = str_para_coordenada(e[0]), e[1]
            pps = parcela_para_str(parcela)

            # No caso de não ter mina, ser uma parcela limpa e que não esteja marcada
            if eh_parcela_limpa(parcela) and not eh_parcela_minada(parcela) \
                    and not eh_parcela_marcada(parcela):

                n_minas = obtem_numero_minas_vizinhas(campo, coord)
                # Indica o número de minas à sua volta, se for 0 então não dirá nada
                pps = str(n_minas) if n_minas != 0 else ' '
                linhas[i+1] += pps
                continue

            linhas[i+1] += pps

        linhas[i+1] += "|"

    return "\n".join(linhas)


def coloca_minas(campo, coord, gerador, numero):
    """
    Esta função modifica o campo de forma a esconder um numero de minas,
    aleatoriamente, através do gerador, de forma a que as minas não sejam
    a coordenada indicada, estejam na sua vizinhança ou já estejam minadas.
    -------------------------------------------------------
    {"campo" x "coordenada" x "gerador" x int} -> {"campo"}
    """

    i = 0
    vizinhas = obtem_coordenadas_vizinhas(coord)
    coord_max = cria_coordenada(
        obtem_ultima_coluna(campo), obtem_ultima_linha(campo))

    while numero > i:
        random = obtem_coordenada_aleatoria(coord_max, gerador)
        random_s = coordenada_para_str(random)

        # Se não resepeitar as condições para ser uma mina no campo, continua à procura de uma coordenada que satisfaça a condição.

        if random == coord or random in vizinhas \
            or not random_s in campo["coords"] \
                or eh_parcela_minada(campo["coords"][random_s]):
            continue
        
        campo["coords"][random_s] = esconde_mina(
            campo["coords"][coordenada_para_str(random)])
        i += 1

    return campo


def limpa_campo(campo, coord):
    """
    Esta função modifica o campo limpando a parcela na coordenada coord e
    devolvendo-a. Se nao houver nenhuma mina vizinha escondida, limpa
    iterativamente todas as parcelas vizinhas tapadas
    -------------------------------------
    {"campo" x "coordenada"} -> {"campo"}
    """

    coord_s = coordenada_para_str(coord)
    coords = campo["coords"]
    vizinhas = obtem_coordenadas_vizinhas(coord)
    coords[coord_s] = limpa_parcela(obtem_parcela(campo, coord))
    
    if eh_parcela_minada(obtem_parcela(campo, coord)):
        return campo

    dicionario = {}  # Dicionário utilizado para atualizar os valores do campo

    if obtem_numero_minas_vizinhas(campo, coord) > 0:
        return campo

    for v in vizinhas:
        v_str = coordenada_para_str(v)
        if eh_coordenada_do_campo(campo, v) and eh_parcela_tapada(obtem_parcela(campo, v)):
            dicionario[v_str] = limpa_parcela(obtem_parcela(campo, v))

    # Atualiza o campo com o dicionário de parcelas limpas
    coords.update(dicionario)

    for v in dicionario.keys():
        v = str_para_coordenada(v)
        # Continua a limpar as vizinhas e por ai a diante
        limpa_campo(campo, v)
    return campo


# 2.2.1


def jogo_ganho(campo):
    """
    Esta função recebe um campo do jogo das minas e devolve True se todas
    as parcelas sem minas se encontram limpas, ou False caso contrario.
    -------------------
    {"campo"} -> {bool}
    """

    parcelas = (ord(obtem_ultima_coluna(campo)) - ord("A") + 1) * obtem_ultima_linha(campo)
    minados = obtem_coordenadas(campo, "minadas")
    limpo = obtem_coordenadas(campo, "limpas")

    return (parcelas - len(minados)) == len(limpo)


def turno_jogador(campo):
    """
    Esta função recebe um campo de minas e oferece ao jogador a opcao de
    escolher uma acao (Limpar ou Marcar) e uma coordenada. Caso o jogador
    escolha limpar e limpe uma parcela que continha uma mina, então 
    retorna False, caso contrário retorna True.
    -------------------
    {"campo"} -> {bool}
    """

    acao, coord = None, None

    if len(obtem_coordenadas(campo, "minadas")) == 0:  # Na primeira jogada é obrigatório limpar
        acao = "L"

    while acao not in ("L", "M"):
        acao = input("Escolha uma ação, [L]impar ou [M]arcar:")

    while not coord or not len(coord) == 3 \
            or not ord("A") <= ord(coord[0]) <= ord("Z") \
            or len(coord[1:]) != 2 or not coord[1:].isdigit() or not 1 <= int(coord[1:]) <= 99 \
            or not str_para_coordenada(coord) \
            or not eh_coordenada_do_campo(campo, str_para_coordenada(coord)):

        coord = input("Escolha uma coordenada:")

    coord = str_para_coordenada(coord)

    if acao == "L":

        if eh_parcela_minada(obtem_parcela(campo, coord)):
            limpa_parcela(obtem_parcela(campo, coord))
            return False

        if len(obtem_coordenadas(campo, "minadas")) != 0:
            limpa_campo(campo, coord)

        else:
            limpa_parcela(obtem_parcela(campo, coord))

    elif acao == "M":
        alterna_bandeira(obtem_parcela(campo, coord))

    return True


def minas(coluna, linha, minas, bits, seed):
    """
    A função minas, sendo a função principal que permite de facto jogar o jogo
    das minas, é uma função que recebe os argumentos necessários para criar um
    campo, um gerador e o número de minas a colocar no campo. A função devolve
    True caso o jogador ganhe o jogo e False caso perca.
    ---------------------------------------
    {str x int x int x int x int} -> {bool}
    """

    if not isinstance(coluna, str) or len(coluna) > 1 \
            or not ord("A") <= ord(coluna) <= ord("Z") \
            or not isinstance(linha, int) or not 1 <= linha <= 99 \
            or not isinstance(bits, int) or bits not in (32, 64) \
            or not isinstance(seed, int) or seed == 0 \
            or not isinstance(minas, int) or minas <= 0 \
            or minas > ((ord(coluna) - ord("A") + 1) * linha - 1) or (ord(coluna) < ord("C") and linha < 3):

        raise ValueError("minas: argumentos invalidos")

    campo = cria_campo(coluna, linha)
    gerador = cria_gerador(bits, seed)

    def _print():
        print(
            f"   [Bandeiras {len(obtem_coordenadas(campo, 'marcadas'))}/{minas}]")
        print(campo_para_str(campo))

    _print()

    playing = True

    while playing and not jogo_ganho(campo):

        playing = turno_jogador(campo)
        limpas = obtem_coordenadas(campo, "limpas")
        marcadas = obtem_coordenadas(campo, "marcadas")

        if len(obtem_coordenadas(campo, "minadas")) == 0:
            coord = None
            if len(limpas) > 0:
                coord = limpas[0]
            if len(marcadas) > 0:
                coord = marcadas[0]
            coloca_minas(campo, coord, gerador, minas)
            limpa_campo(campo, coord)

        if playing and jogo_ganho(campo):  # Jogo ganho
            _print()
            print("VITORIA!!!")
            return True
        _print()

    # Jogo perdido
    print("BOOOOOOOM!!!")

    return False