#Se importa la libreria "time"
import time
#Se imprime un texto que informa el inicio de programa
print("Iniciando contador binario de 0 a 15:")

#----Inicio seccion estetica
#La siguiente seccion esta pensada para hacer mas amigable el programa para el usuario
#los contadores tiene fines esteticos y mejorar la comprencion del programa
time.sleep(2) 
print ("Cargando....")
time.sleep (3)
#----Fin de seccion estetica


#Iniciamos un contador en 0
numero = 0

#Inicio del bucle while

while numero <= 15:
    n = numero
    binario = ""
    if n == 0:
        binario = "0"
    else:
        #Inicio de algoritmo para pasar de decimal a binario
        #Algoritmo: dividir por 2 y guardar los restos siemmpre que n > 0
        while n > 0:
            resto = n % 2
            binario = str(resto) + binario
            n = n // 2

    print(f"{numero} -> {binario}")
    time.sleep(1)
    numero += 1
    
#Fin del bucle while
#Fin del programa