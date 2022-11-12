from ex5 import bissexto

def dia_mes(mes, ano):
    m30 = ("abr", "jun", "set", "nov")
    m31 = ("jan", "mar", "mai", "jul", "ago", "out", "dez")

    if mes in m30:
        return 30
    if mes in m31:
        return 31

    ano_bissexto = bissexto(ano)

    if ano_bissexto:
        return 29
    return 28
    

print(dia_mes("fev", 2005))