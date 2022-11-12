# 2.1.1

# def cria_gerador(b,s):
#     if not isinstance(b, int) or (b != 32 and b != 64) or not isinstance(s, int):
#         raise ValueError("cria_gerador: argumentos invalidos")
#     if b == 32:
#         s ^= ( s << 13 ) & 0xFFFFFFFF
#         s ^= ( s >> 17 ) & 0xFFFFFFFF
#         s ^= ( s << 5 ) & 0xFFFFFFFF
#     else:
#         s ^= ( s << 13 ) & 0xFFFFFFFF
#         s ^= ( s >> 7 ) & 0xFFFFFFFF
#         s ^= ( s << 17 ) & 0xFFFFFFFF
#     return s

def cria_gerador(b,s):
    if not isinstance(b, int) or (b != 32 and b != 64) or not isinstance(s, int):
        raise ValueError("cria_gerador: argumentos invalidos")
    return {"b":b, "s": s}

def cria_copia_gerador(g):
    return g.copy()

def obtem_estado(g):
    return g["s"]

def define_estado(g, s):
    g["s"] = s
    return s

def atualiza_estado(g):
    s = g["s"]
    if g["b"] == 32:
        s ^= ( s << 13 ) & 0xFFFFFFFF
        s ^= ( s >> 17 ) & 0xFFFFFFFF
        s ^= ( s << 5 ) & 0xFFFFFFFF
    else:
        s ^= ( s << 13 ) & 0xFFFFFFFF
        s ^= ( s >> 7 ) & 0xFFFFFFFF
        s ^= ( s << 17 ) & 0xFFFFFFFF
    return s

def eh_gerador(g):
    return isinstance(g, dict) and len(g) == 2 and "b" in g and "s" in g and type(g["s"]) == type(g["b"]) == int

def cria_copia_gerador(g): 
    return g[:]

def geradores_iguais(g1, g2):
    return g1 == g2

def gerador_para_string(g):
    return f'xorshift{g["b"]}(s={g["s"]})'

# 2.1.2

def cria_coordenada(col, lin):
    if not isinstance(lin, int) or not isinstance(col, str) or not 99 >= lin >= 1 or not 90 >= ord(col) >= 65:
        raise ValueError("cria_coordenada: argumentos invalidos")
    return {"col": col, "lin": lin}

def obtem_coluna(coordenada):
    return coordenada["col"]

def obtem_linha(coordenada):
    return coordenada["lin"]

def eh_coordenada(arg):
    return isinstance(arg, dict) and len(arg) == 2 and "col" in arg and "lin" in arg and isinstance(arg["col"], str) and isinstance(arg["col"], int)

def coordenadas_iguais(c1, c2):
    return c1 == c2

def coordenada_para_str(c):
    numero = obtem_linha(c) if obtem_linha(c) >= 10 else f'0{obtem_linha(c)}'
    return f"{obtem_coluna(c)}{numero}"

def str_para_coordenada(c):
    return cria_coordenada(c[:1], c[1:])
