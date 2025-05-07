edad = int(input("Ingrese su edad:"))

if edad < 12:
    print ("Categoria:Niño/a")
elif edad >= 12 and edad<18:
    print ("Categoria:Adolescente")
elif edad >=18 and edad<30:
    print ("Categoria:Adulto/a joven")
else:
    print ("Categoria:Adulto/a")