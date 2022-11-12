from ex2 import explode

def num_para_seq_cod(numero):
    if type(numero) != int:
        raise ValueError("elemento não inteiro")

    tuplo = explode(numero)
    novo_tuplo = ()
    for element in tuplo:
        if element % 2 == 0:
            if element == 8:
                novo_tuplo += (0, )
            else:
                novo_tuplo += (element+2, )
        else:
            if element == 1:
                novo_tuplo += (9, )
            else:
                novo_tuplo += (element-2, )
    return novo_tuplo

print( num_para_seq_cod(1234567890) )