numero = int(input("Ingrese un número entero: "))

numero_absoluto = abs(numero)
numero_invertido = 0

while numero_absoluto > 0:
    digito = numero_absoluto % 10           # Extrae el último dígito
    numero_invertido = numero_invertido * 10 + digito  # Lo agrega al nuevo número
    numero_absoluto = numero_absoluto // 10 # Quita el último dígito

# Si el número original era negativo, lo invertimos también
if numero < 0:
    numero_invertido = -numero_invertido

print("Número invertido:", numero_invertido)
