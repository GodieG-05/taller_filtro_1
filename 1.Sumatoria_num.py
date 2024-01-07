import os
rta = "SI"
while rta.upper() == "SI":
    print("""*************************************************
        ****** Bienvenido a tu calculadora ******      
    Escribe 3 numeros enteros positivos y te diré su suma 
        """)
    sum = 0
    for i in range(3):
        num = int(input(f"Digita el número {i+1}: "))
        sum = sum + num
    print(f"la sumatoria de los numeros ingresados es: {sum}")
    os.system("pause")
    rta = input("¿Desea ingresar otros 3 numeros y averiguar su suma? Si o No :)")
    os.system("cls")
