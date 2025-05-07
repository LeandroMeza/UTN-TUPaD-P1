frase = input ("Ingrese una frase: ")

ultcaracter = len(frase)

vocal = (frase[ultcaracter-1])

if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
    print (f"{frase} !!!.")
else:
    print (frase)


