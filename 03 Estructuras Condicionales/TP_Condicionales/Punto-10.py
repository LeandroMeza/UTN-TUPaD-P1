from datetime import date

# Pide los datos al usuario
hemisferio = input("En qué hemisferio estás? (N/S): ").upper()

dia = int(input("Ingrese Dia: "))
mes = int(input("Ingrese Mes: "))
año = int(input("Ingrese Año: "))

fecha = date(año, mes, dia)

# Define las fechas de las estaciones
invierno1 = date(año, 12, 21)
invierno2 = date(año + 1, 3, 20)

primavera1 = date(año, 3, 21)
primavera2 = date(año, 6, 20)

verano1 = date(año, 6, 21)
verano2 = date(año, 9, 20)

otono1 = date(año, 9, 21)
otono2 = date(año, 12, 20)

# Decide la estación según la fecha y el hemisferio
if fecha >= invierno1 or fecha <= date(año, 3, 20):
    if hemisferio == "N":
        print("Es invierno")
    elif hemisferio == "S":
        print("Es verano")
elif fecha >= primavera1 and fecha <= primavera2:
    if hemisferio == "N":
        print("Es primavera")
    elif hemisferio == "S":
        print("Es otoño")
elif fecha >= verano1 and fecha <= verano2:
    if hemisferio == "N":
        print("Es verano")
    elif hemisferio == "S":
        print("Es invierno")
elif fecha >= otono1 and fecha <= otono2:
    if hemisferio == "N":
        print("Es otoño")
    elif hemisferio == "S":
        print("Es primavera")
else:
    print("Datos no válidos o hemisferio incorrecto")
