n = 5
number = 2
pares = 0
check = 2

def primo(numero):
    i = 2
    s = True

    if numero == 2:
        return True

    while numero > i:
        if numero % i == 0:
            s = False
            return s    

        i +=1

        if numero == i:
            return s

while pares < n:
    if primo(check) and primo(check + 2):
        pares += 1
        print(check, check + 2)
    check += 1