x = int(input("Numero ? "))

# def misterio (num):
#     i = 0
#     numero1 = num
#     numero2 = 0

#     while num > 0:

#         alg = num % 10

#         if i == 0:
#             n1 = alg
#         if i == 2:
#             n2 = alg

#         numero2 = numero2 * 10 + alg
#         i+=1
#         num //=10

#     if abs(n2-n1) <= 1:
#         raise ValueError("A diferenca entre o primeiro digito e o terceiro tem de ser superior a 1.")

#     if i > 3 :
#         raise ValueError("O numero so pode ter 3 digitos")

#     ns = abs(numero1 -  numero2)
#     ns1 = ns
#     nsi = 0

#     while ns1 > 0:

#         alg = ns1 % 10
#         nsi = nsi * 10 + alg

#         ns1 //= 10

#     print(ns + nsi)

# misterio(x) # Exercicio 10 sem funcao auxiliar

def misterio (num):
    def reverse(y):
        numero = 0
        while y > 0:
            numero = y % 10 + numero * 10
            y //= 10
        return numero
    ni = reverse(num)
    ns = abs(num - ni)

    if 1000 < ns or ns < 100:
        return "Condições não verificadas"

    nsi = reverse(ns)


    
    return  ns + nsi
print(misterio(x))