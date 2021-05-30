#Exercício 1

s = 0
for x in range(3,334,3):
    s = s + x
print ("A soma S = 3 + 6 + 9 + ... + 333 é: ", s)
print("\n")

#Exercício 2

aluno = 0
soma = 0
while aluno < 10:
    aluno = aluno + 1
    nota = float(input("Digite a nota do aluno " +str(aluno)+ ": "))
    soma = soma + nota
media = soma/10
print("\nMédia dos alunos: ", media)
print("\n")

#Exercício 3

num = int(input("Digite um número de 1 a 10: "))
print("\n")
print("Tabuada do " + str(num)+ ": ")

for i in range(0,11,1):
    print(num, " x ", i, " = ", num*i)

