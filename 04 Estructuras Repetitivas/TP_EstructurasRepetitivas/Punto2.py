numero = int(input("Ingrese un número entero: "))

#Asegurarse de que el número sea positivo
numero_absoluto = abs(numero)

#Contador de dígitos
contador = 0

#Si el número es 0, tiene 1 dígito
if numero_absoluto == 0:
    contador = 1
else:
    while numero_absoluto > 0:
        numero_absoluto = numero_absoluto // 10  #Elimina el último dígito
        contador += 1

print("La cantidad de dígitos es:", contador)
