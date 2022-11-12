def filtra_pares(tuplo):
    result = ()
    for element in tuplo:
        if type(element) != int:
            raise ValueError("elemento não inteiro")
        if element % 2 == 0:
            result += (element, )
        

    return result

#print(filtra_pares((2, 5, 6, 7, 9, 1, 8, 8)))