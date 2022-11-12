def cria_rac(n,d):
    assert d > 0
    return {"num": n, "den": d}

def num(r):
    return r["num"]

def den(r):
    return r["den"]

def eh_racional(r):
    return isinstance(r, dict)\
        and len(r) == 2 \
        and "num" in r and "den" in r\
        and isinstance(r["num"], int) and isinstance(r["den"], int) \
        and r["den"] > 0

def eh_rac_zero(r):
    return eh_racional(r) and num(r) == 0

def rac_iguais(r1, r2):
    return eh_racional(r1) and eh_racional(r2) \
        and num(r1) * den(r2) == num(r2) * den(r1)

def escreve_rac(r):
    return f"{num(r)}/{den(r)}"

def produto_rac(r1, r2):
    return cria_rac(num(r1)*num(r2), den(r1)*den(r2))