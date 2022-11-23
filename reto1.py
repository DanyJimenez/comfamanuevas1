
'''
nombre
cedula
pedido
precio de la hamburguesa
calcule la cantidad segun pedido
*****
hamburguesas el corral
**********
hamburg pedida: cantidad
nombre hamburguesa
2. cantidad
3.total
'''
print("HAMBURGUESAS EL CORRAL")
print("*"*20)

nombreUsuario = input("Digite su nombre: ")
documentoUsuario = input("Digite su documento: ")
doble = 20000
vegetariana = 10000
sencilla = 9000
#opciones = (vegetariana,sencilla,doble)
pedido = input(f"¿Cuál hamburguesa desea, {nombreUsuario}? Hamburguesa Sencilla: ${sencilla}, Hamburguesa Doble: ${doble}, Hamburguesa Vegetariana: ${vegetariana} ")
pedido = pedido.lower()
cantidad = int(input(f"¿Cuántas hamburguesas desea pedir, {nombreUsuario}? "))
print("*"*20)
print(f"{nombreUsuario}, su pedido es {cantidad}  hamburguesa(s) {pedido} con un valor de ${pedido}")
