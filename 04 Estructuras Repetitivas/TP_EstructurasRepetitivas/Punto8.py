
cantidad_numeros = 100

# Contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i + 1}: "))

    # Par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Positivo o negativo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1


print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)
