print ("Su contraseña debe tener entre 8 y 14 caracteres !!!!.")
password = input("Ingrese una contraseña:")

cantcaracteres= len(password)

if cantcaracteres >=8 and cantcaracteres <= 14:
    print("Contraseña Valida")
else:
    print("Cantidad de caracteres incorrectos")