import random
import os
print("""
ESTE ES EL PROGRAMA QUE IMPRIME NÚMEROS Y TE DA INFORMACIÓN
""")

numeros = []
numPar = []
numImpar = []
menor10 = 0
num20_50 = 0
mayor100 = 0
num = 0
rta = "S"
while rta in ["S","s"]:
    num = int(input("Ingrese un numero entero: "))
    numeros.append(num)
    numIng = len(numeros)

    if (num % 2 == 0 and num !=0):
        numPar.append(num)

    if num % 2 == 1:
        numImpar.append(num)
        
    if num < 0:
        menor10 = menor10 + 1
        print(numeros)
        print(f"El total de numeros ingresados fue {numIng}")
        print(f"El total de numeros pares ingresados fue {len(numPar)}")
        try:
            promPar = sum(numPar)/len(numPar)
            print(f"El promedio de numeros pares fue {promPar}")
        except ZeroDivisionError:
            print("*** Como NO se digitaron numeros pares, su promedio es 0")
        try:
            promImpar = sum(numImpar)/len(numImpar)
            print(f"El promedio de numeros impares fue {promImpar}")
        except ZeroDivisionError:
            print("*** Como NO se digitaron numeros impares, su promedio es 0")
        print(f"El total de numeros menores a 10 fue {menor10}")
        print(f"El total de numeros entre 20 y 50 fue {num20_50}")
        print(f"El total de numeros mayores a 100 fue {mayor100}")

    if num < 10:
        menor10 = menor10 + 1
        
    if (num >= 20 and num <= 50):
        num20_50 = num20_50 + 1
        
    if num > 100:
        mayor100 = mayor100 + 1
        
    rta = input("¿Desea ingresar otro numero? s(Si) o n(No)").upper()
    os.system("cls")



