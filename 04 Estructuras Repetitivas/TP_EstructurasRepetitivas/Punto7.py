numero = int(input("Ingrese un número entero positivo: "))

while numero < 0:
    numero = int(input("Por favor ingrese un número positivo: "))

acumulador = 0

for i in range(1, numero + 1):
    acumulador += i

print("La suma de los números entre 0 y", numero, "es:", acumulador)
