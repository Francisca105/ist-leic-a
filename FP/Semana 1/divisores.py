num = int(input())
div = 1

while True:
    print(div, num)
    print(num % % div)

    if num % div != 0:
        num = num // div
        #print(div, num)
    else:
        #print(div, num)
        div += 1
    break
