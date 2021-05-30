nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2)/2

if media >= 6:
    print("\nAprovado!\n")
else:
    print("\nReprovado!\n")

#Exercício 2
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

media1 = (n1 + n2)/2

if media1 > 6:
    print("\nAprovado!")
elif media1 < 4:
    print("\nReprovado!")
else:
    print("Exame!")