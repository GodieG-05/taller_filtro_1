import os
def informe_riesgos(ciudades:list):
    os.system("cls")
    header = """
    **************************************
    *         INFORME DE RIESGOS         *
    **************************************
    """
    print(header)
    for item in ciudades:
        indice = ciudades.index(item)
        prom = sum(ciudades[indice][2])/len(ciudades[indice][2])
        if prom <= 2.5:
            ciudades[indice][4].append("Amarillo [sin riesgo]")
        elif prom > 2.5 and prom <= 4.5:
            ciudades[indice][4].append("Naranja [riesgo medio]")
        elif prom > 4.5:
            ciudades[indice][4].append("Rojo [riesgo alto]")
    print(ciudades)
