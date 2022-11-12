number = 1234567890
soma = 0

while number > 0:
    dig = number % 10
    number //=10
    if (dig % 2) == 0:
        soma += dig * dig
      
print(soma)