res = 0

while True:
    x = eval(input("Num: "))
    if x == -1:
        break
    else:
        res = res * 10 + x

print(res)