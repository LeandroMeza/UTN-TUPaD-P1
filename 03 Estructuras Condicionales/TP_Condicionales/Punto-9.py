magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print ("'Muy Leve'(imperceptible)")
elif magnitud >= 3 and magnitud<4:
    print ("'Leve'(Ligeramente perceptible)")
elif magnitud >=4 and magnitud<5:
    print ("'Moderado' (Sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud<6:
    print ("'Fuerte'(Puede causar daños en estructuras)")
elif magnitud >= 6 and magnitud<7:
    print ("'Muy Fuerte'(Puede causar daños significativos)")
else:
    print ("'Extremo'(Puede causar daños a gran escala)")