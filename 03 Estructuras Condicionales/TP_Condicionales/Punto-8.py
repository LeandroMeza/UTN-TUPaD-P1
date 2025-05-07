
nombre = input ("Ingrese su nombre: ")
print("A continuacion elegira la opcion de formato que quiera.")
print("Si quiere su nombre en mayusculas ingrese el numero 1")
print("Si quiere su nombre en minusculas ingrese el numero 2")
print("Si quiere su nombre con la inicial em mayuscula ingrese el nuemro 3")
opcion = int(input("Ingrese el numero de la opcion: "))

if opcion == 1:
    nmay = nombre.upper ()
    print (nmay)
elif opcion == 2:
    nmin =nombre.lower ()
    print (nmin)
elif opcion == 3:
    ninicial = nombre.title ()
    print (ninicial)
else:
    print ("Opcion no valida") 