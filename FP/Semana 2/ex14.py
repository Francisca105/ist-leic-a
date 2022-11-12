n = eval(input("Numero "))
res = 0
while n > 0:
    d = n % 10
    n //=10
    res += d
print(res)
