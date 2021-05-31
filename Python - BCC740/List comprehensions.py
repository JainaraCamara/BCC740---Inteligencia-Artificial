#Números de 1 a 1000 que são divisíveis por 8

nums = [i for i in range(1,1001)]
result = [nums for nums in range(1001) if nums % 8 == 0]

print(result)
print("\n")

#Números de 1 a 1000 que possuem o dígito 6
res = [print (i) for i in nums if str(i).count("6") > 0]
print("\n")


#Número de espaços na string sentence
sentence = "Practice Problems to Drill List Comprehension in Your Head."
esp = [ + 1 for i in sentence if i == " "]
print ("Número de espaços na string: ", sum(esp))
print("\n")

#Removendo as vogais da string sentence

frase = list(sentence)
[frase.remove(i) for i in frase if i == "a"] 
[frase.remove(i) for i in frase if i == "e"] 
[frase.remove(i) for i in frase if i == "i"] 
[frase.remove(i) for i in frase if i == "o"] 
[frase.remove(i) for i in frase if i == "u"] 
print(frase)
print("\n")

#Palavras da string com menos de 5 letras

sentence = sentence.split(" ")
[print(i) for i in sentence if len(i) < 5]
print("\n")

#Tirando o "."
sentence = [i.replace(".", "") for i in sentence]
[print(i) for i in sentence if len(i) < 5]