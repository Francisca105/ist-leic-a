all = 0
tudo = 0

pos = 0
neg = 0

while True:
    x = int(input("Nota:\n(Digite -20 ou uma acima de 20 para terminar)\n? "))
    all += 1
    if x == -20 or x > 20:
        break
    if x > 9:
        print("Teve positiva")
        tudo += 1
        pos += 1
    else:
        print("Teve negativa")
        neg += 1
    

print("Média das postivas:", (tudo/all) * 100 , "%")
print("Percentagem de alunos com positiva:", (pos/(pos+neg)) * 100 , "% (",pos,")")