#Se piden dos numeros al usuario
numero1 = int (input("Ingrese un valor: " ))
numero2 = int (input("Ingrese un valor: " ))

# Se crea un acumulador
acumulador = 0

#Este for suma los valores entre numero1 y numero2
for i in range (numero1,numero2+1):
    numero3 = i 
    acumulador += i
print (f"La suma de los valores entre {numero1} y {numero2} es {acumulador}")