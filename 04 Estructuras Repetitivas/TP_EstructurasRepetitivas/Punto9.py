cantidad_numeros = 100

acumulador = 0

for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    acumulador += numero

media = acumulador / cantidad_numeros

print("La media de los", cantidad_numeros, "números ingresados es:", media)
