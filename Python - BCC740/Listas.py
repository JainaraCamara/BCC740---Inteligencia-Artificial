L = [5, 7, 2, 9, 4, 1, 3]

print("Lista: ", L)
print("\nTamanho da lista: ", len(L))
print("Maior valor da lista: ", max(L))
print("Menor valor da lista: ", min(L))
print("Soma dos elementos da lista: ", sum(L))

L.sort()
print("Lista em ordem crescente: ", L)

L.reverse()
print("Lista em ordem decrescente: ", L)