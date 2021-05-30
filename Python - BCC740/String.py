#1)Considere a string A = "Um elefante incomoda muita gente". Que fatia corresponde a "elefante
#incomoda"

A = "Um elefante incomoda muita gente"
print(A[3:20])

#Escreva um programa que solicite uma frase ao usuário e escreva a frase toda em maiúscula e 
#sem espaços em branco

frase = input("Digite uma frase: ")
print(frase.lower().replace(" ", ""))