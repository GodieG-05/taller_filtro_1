import os
def buscar_sismos_por_ciudad(ciudades:list):
    header = """
    **************************************
    *   BUSQUEDA DE SISMOS POR CIUDAD    *
    **************************************
    """
    print(header)
    os.system("cls")
    nombre = input("Ingrese nombre de ciudad: ")
    for item in ciudades:
        if nombre in item:
            print(item)
        else:
            print("La ciudad no se encuentra registrada")