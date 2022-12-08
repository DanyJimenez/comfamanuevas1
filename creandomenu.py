
from ast import Num
from ntpath import join


opcion = 100

print("Empanadas El machetico")
print("Elija, por favor, una de las siguientes opciones:")
print("***********************\n")

print("1. Registrar empanada ")
print("2. Ver empanada empanada ")
print("0. Salir ")


empanadas = []



while opcion != 0:
    opcion = int(input("Digita una opción: "))
    if opcion == 1:
        empanada = input("Digite la(s) empanada(s) que desea registrar: ")
        empanadas.append(empanada)
    elif opcion == 2:
        print("PEDIDO:")
        for empanada in empanadas:
            if len(empanadas) > 1:
                print(f"Empanada de {empanada}")
            else:
                print(f"Usted pidió una empanada de {empanada}")
    elif opcion == 0:
        break
    else:
        print("Apreciado usuario, debe seleccionar  una opción válida.")

