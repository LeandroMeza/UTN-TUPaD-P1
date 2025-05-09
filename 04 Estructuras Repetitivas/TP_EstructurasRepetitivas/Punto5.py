import random

# Genera un número aleatorio entre 0 y 9
numero_secreto = random.randint(0, 9)

intentos = 0
adivinanza = -1  # Valor inicial que no sea igual al secreto

while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1

print("¡Correcto! El número era", numero_secreto)
print("Lo lograste en", intentos, "intento(s).")
