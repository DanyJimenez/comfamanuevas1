opcion = 100

print("Empanadas El machetico")
print("***********************\n")

print("1. Registrar empanada ")
print("2. Ver empanada empanada ")
print("0. Salir ")

empanadas = []

while opcion != 0:
    opcion = int(input("Digita una opción: "))
    if opcion == 1:
        empanada = input("Digite el nombre de la empanada que quiere registrar: ")
        empanadas.append(empanada)
    elif opcion == 2:
        for empanada in empanadas:
            print(f"La empanada que pediste es {empanada}")
    elif opcion == 0:
        break
    else:
        print("Apreciado usuario, debe seleccionar  una opción válida.")