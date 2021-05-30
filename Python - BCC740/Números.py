x = int(input("X: "))
y = int(input("Y: "))

if x != y:
    z = ((x**2)+(y**2))/((x-y)**2)
    print("O valor de Z é:", int(z))

else:
    print("IMPOSSÍVEL CALCULAR O VALOR DE Z: NÃO EXISTE DIVISÃO POR 0!")