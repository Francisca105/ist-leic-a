def implodeFor(tuplo):
    number = 0
    for element in tuplo:
        if type(element) != int:
            raise ValueError("elemento não inteiro")
        number = number * 10 + element

    return number

#print( implodeFor((3, 4, 0, 0, 4)) )
#print( implodeFor((2, "a", 5)) )

def implodeWhile(tuplo):
    number = 0
    i = 0
    length = len(tuplo)
    while i < length:
        element = tuplo[i]
        if type(element) != int:
            raise ValueError("elemento não inteiro")
        number = number * 10 + element
        i+=1

    return number

#print( implodeWhile((3, 4, 0, 0, 4)) )
#print( implodeWhile((2, "a", 5)) )