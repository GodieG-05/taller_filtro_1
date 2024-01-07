import os
def registrar_sismo(ciudades: list):
    os.system("cls")
    header = """
    **************************************
    *         REGISTRO DE SISMOS         *
    **************************************
    """
    print(header)
    nombre = input("Nombre de la ciudad: ")
    for item in ciudades:   
        if nombre not in item:
            print("\n[!] Error: ciudad no encontrada.\n")
        else:
            indice = ciudades.index(item)
            if len(ciudades[indice][2]) == 5:
                print("*****\n*****")
                print(f"La ciudad {nombre} ya cuenta con 5 sismos registrados")   
            else:
                print("Debe ingresar 5 sismos")
                for i in range(5):
                    while True:
                        try:
                            sismo = float(input(f"Ingrese el {i+1}° sismo en la escala de richter: "))
                            ciudades[indice][2].append(sismo)
                        except ValueError:
                            print("*****\n*****")
                            print ("[!] Error en el dato ingresado\n***Se espera un numero entero o decimal")
                        else:
                            break
                print("*****\n*****")
                print(ciudades[indice][:3])