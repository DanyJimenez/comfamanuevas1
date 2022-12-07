# quiero recoger 20 números y cada entrada se va llamar número

numeros = []

for numero in range(20):
    numeros.append(int(input("Ingrese un número: ")))

print(numeros)

for numero in numeros:
    print(numero)