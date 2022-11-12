x = int(input("Indique o x:"))
n = int(input("Indique o n:"))

result = 1
last_item = 1
m = 1

while m <= n:
    item = last_item * (x / m)
    last_item = item
    result += item
    m+=1

print('O valor da soma é', result)

def ftl(i):
    f=1
    while i > 0:
        f = f * i
        i -= 1
    return f

print(ftl(8))