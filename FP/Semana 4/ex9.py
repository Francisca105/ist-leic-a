def explodeStr(str):
    tuplo = ()
    for element in str:
        tuplo+=(element, )
        #number = number * 10 + element
    return tuplo

def reconhece(idt):
    letras = ("A", "B", "C", "D")
    numeros = ("1", "2", "3", "4")
    tudo = letras + numeros

    if not idt.startswith(letras):
        return False

    if not idt.endswith(numeros):
        return False

    exploded = explodeStr(idt)
    number = False

    for e in exploded:
        if e.isnumeric():
            number = True
        elif number:
            return False
    
    if all(ch in tudo for ch in idt):
        return True

    

#print(reconhece("A1"),reconhece("ABBBBCDDDD23311"),reconhece("ABBBBCD34134DDD23311"),reconhece("ABC12C"))