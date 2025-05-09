
acumulador = 0
#El while Sumara los numeros ingresados hasta que se presione 0
while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    acumulador += numero

print("La suma total es:", acumulador)
