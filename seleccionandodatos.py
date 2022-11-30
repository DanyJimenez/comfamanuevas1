'''
Entradas del problema:



'''

nivelDeAgua = int(input("¿Cuál es el nivel de agua? "))

#Evaluando caminos múltiples

if nivelDeAgua <= 100:
    print("Bajo nivel de agua")
elif nivelDeAgua >100 and nivelDeAgua <400:
    print("Operación óptima")
elif nivelDeAgua >=400:
    print("Peligro")
else:
    print("Nivel de agua no válido")