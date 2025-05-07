from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1,100) for i in range (50)]

lista1= mode(numeros_aleatorios)
lista2= median(numeros_aleatorios)
lista3= mean(numeros_aleatorios)

print(lista1)
print(lista2)
print(lista3)