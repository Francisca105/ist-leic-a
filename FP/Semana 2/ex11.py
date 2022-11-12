m = 1
resultado = 0
n = eval(input("Int +: "))

while n > 0:
    resultado = resultado * m +n % 10
    n //= 10
    m = m*10
print(resultado)