y = int(input("Escreva um inteiro\n? "))
x = y
zeros = 0

zero = False

def checkzero (x):
    dig = x % 10
    if dig == 0:
        return True
    else:
        return False

while x > 0:
    check = checkzero(x)
    x //= 10
    if (check and checkzero(x)) or (check and zero):
        zeros += 1
        zero = True
    else:
        zero = False
    



#print(f"O número {y} tem {zeros} zeros de seguida.")
print(zeros)