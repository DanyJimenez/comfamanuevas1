mes = input("¿En qué mes estás? ")

if mes == "marzo" or mes == "abril" or mes == "mayo":
    print(f"Si el mes es {mes}, estás en primavera")
elif mes == "junio" or mes == "julio" or mes == "agosto":
    print(f"Si el mes es {mes}, estás en verano")
elif mes == "septiembre" or mes == "octubre" or mes == "noviembre":
    print(f"Si el mes es {mes}, estás en otoño")
elif mes == "diciembre" or mes == "enero" or mes == "febrero":
    print(f"Si el mes es {mes}, estás en invierno")
else:
    print("Introduce de nuevo el mes!")


