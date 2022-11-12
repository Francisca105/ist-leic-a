n = 0
maior = None

greater = False
while n < 3:
    x = int(input(f"Escreva o {n+1}º número: "))
    n += 1
    if maior is None or x > maior:
        maior = x

print(f"O maior número é {maior}")