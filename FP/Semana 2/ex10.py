n = int(input("? "))
resultado = 0
fator = 1

while True:
    if n != 0:
        alg = n%10
        n = n//10
        print(n)
        if alg % 2 != 0:
            resultado = fator * resultado + alg
            fator *= 10
print("Resultado", resultado)