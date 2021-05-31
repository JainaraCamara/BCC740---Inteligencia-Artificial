#Números de 1 a 1000 que são divisíveis por 8

nums = [i for i in range(1,1001)]
result = [nums for nums in range(1001) if nums % 8 == 0]

print(result)

#Números de 1 a 1000 que possuem o dígito 6
