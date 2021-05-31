#Exercício 1

def desenho(N):
    for i in range(N):
        print (end = '_')

n = int(input("Digite um número: "))
desenho(n)
print("\n")

#Exercício 2 

def list(L):
    for i in range (len(L)):
        print(i + 1," - ",L[i])

    
list(["abacate","melão","abacaxi","melão", 9, 6.3])
print("\n")


#Exercício 3

def media(Lnum):
    media = sum(Lnum)/len(Lnum)
    return media

print("Média dos valores: ", media([10,10,5,5,5]))