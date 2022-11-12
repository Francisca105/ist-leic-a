from ex9 import explodeStr

def implodeStr(tuplo):
    string = ""
    for element in tuplo:
        string+=element
    return string

def codifica(string):
    tuplo = explodeStr(string)
    impares = tuplo[::2]
    pares = tuplo[1::2]
    #print(pares,impares)
    return implodeStr(impares + pares)

#print(codifica('abcde'))

def descodifica(string):
    tuplo = explodeStr(string)
    length = len(tuplo)
    min = round(length//2)

    if length % 2 != 0:
        min += 1
    
    impares = tuplo[:min]
    pares = tuplo[min:]
    res = ()
    
    for i in range(min):
        if i <= (len(pares)-1):
            res += (impares[i], pares[i])
        else:
            res += (impares[i], )

    return implodeStr(res)


print(descodifica('acebd'))