n = 1
s = 1

while s < 10:
    print(f"{n} x 8 + {s} = {n*8+s}")
    n = n*10+ n%10+1
    s += 1