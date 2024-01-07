import os
def registrar_ciudad(ciudades: list):
    os.system("cls")
    header = """
    **************************************
    *        REGISTRO DE CIUDADES        *
    **************************************
    """
    print(header)
    rta = "S"
    while rta in ["S","s"]:
        if len(ciudades) == 5:
            print("****\****")
            print("Máximo 5 ciudades pueden ser registradas")
            break
        else:
            nombre = input(f"Ingrese el nombre de la ciudad: ")
            ciudad = [nombre,"Sismos ->",[],"Nivel de riesgo ->",[]]
            ciudades.append(ciudad)
            rta = input("¿Desea agregar otra ciudad? S(si) o N(no)")            
