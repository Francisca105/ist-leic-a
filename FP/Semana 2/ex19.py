valor = 60

notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_5 = 0

moedas_2 = 0
moedas_1 = 0
moedas_05 = 0
moedas_02 = 0
moedas_01 = 0
moedas_005 = 0
moedas_002 = 0


while valor > 0:
    if valor >= 50:
        valor -= 50
        notas_50 += 1

    if valor >= 20:
        valor -= 20
        notas_20 += 1

    if valor >= 10:
        valor -= 10
        notas_10 += 1

    if valor >= 5:
        valor -= 5
        notas_5 += 1

    if valor >= 2:
        valor -= 2
        moedas_2 += 1

    if valor >= 1:
        valor -= 1
        moedas_1 += 1

    if valor >= 0.5:
        valor -= 0.5
        moedas_05 += 1

    if valor >= 0.2:
        valor -= 0.2
        moedas_02 += 1

    if valor >= 0.1:
        valor -= 0.1
        moedas_01 += 1

    if valor >= 0.05:
        valor -= 0.05
        moedas_005 += 1

    if valor >= 0.02:
        valor -= 0.02
        moedas_002 += 1

print(notas_50, notas_20, notas_10, notas_5, moedas_2, moedas_1,
      moedas_05, moedas_02, moedas_01, moedas_005, moedas_002)
