import os

def dependencia_con_mayor_produccion_de_CO2(dependencias: dict) -> str:
    header = """
    **************************************
    *       MAYOR PRODUCCIÓN DE CO2      *
    **************************************
    """
    print(header)
    emisiones_totales = 0.0
    dependencia = ""
    for clave, valor in dependencias.items():
        if sum(valor["CO2 producido"]) > emisiones_totales:
            emisiones_totales = sum(valor["CO2 producido"])
            dependencia = clave
    return dependencia,emisiones_totales


def ver_CO2_producido(dependencias: dict) -> float:
    header = """
    **************************************
    *   VISUALIZACIÓN DE CO2 PRODUCIDO   *
    **************************************
    """
    print(header)
    emisiones_totales = 0.0
    for clave, valor in dependencias.items():
        emisiones_totales += sum(valor["CO2 producido"])
    return emisiones_totales


def registrar_consumo(dependencias: dict) -> None:
    header = """
    **************************************
    *        REGISTRO DE CONSUMO         *
    **************************************
    """
    print(header)
    nombre = input("Nombre de la dependencia: ")
    if not nombre in dependencias:
        print("\n[!] Error: Dependencia no encontrada.\n")
        return
    for i in range(len(dependencias[nombre]["Dispositivos"])):
        print(f"Dispositivo: {dependencias[nombre]['Dispositivos'][i]}")
        if dependencias[nombre]["tipo"][i] == 1:
            while True:
                try:
                    potencia = float(input("Potencia del dispositivo (KWh): "))
                except ValueError:
                    print("*****\n*****")
                    print ("[!] Error en el dato ingresado\n***Se espera un numero entero o decimal")
                else:
                    break
            while True:
                try:
                    tiempo_de_uso = float(input("Tiempo de uso (h): "))
                except ValueError:
                    print("*****\n*****")
                    print ("[!] Error en el dato ingresado\n***Se espera un numero entero o decimal")
                else: 
                    break
            consumo = (potencia * tiempo_de_uso) / 1000
            dependencias[nombre]["CO2 producido"].append(consumo * 0.05)
        elif dependencias[nombre]["tipo"][i] == 2:
            while True: 
                try:
                    recorrido = float(input("Kilómetros recorridos: "))
                except ValueError:
                    print("*****\n*****")
                    print ("[!] Error en el dato ingresado\n***Se espera un numero entero o decimal")
                else: 
                    break
                dependencias[nombre]["CO2 producido"].append(recorrido * 0.5)


def registrar_dependencia(dependencias: dict) -> None:
    header = """
    **************************************
    *      REGISTRO DE DEPENDENCIAS      *
    **************************************
    """
    print(header)
    nombre = input("Nombre de la dependencia: ")
    dependencias[nombre] = {"Dispositivos": [], "tipo": [], "CO2 producido": [], "": []}
    while True:
        try:
            numero_de_dispositivos = int(input(f"Número de dispositivos de {nombre}: "))
        except ValueError:
            print("*****\n*****")
            print ("[!] Error en el dato ingresado\n***Se espera un numero entero")
        else:
            break
    for i in range(numero_de_dispositivos):
        dependencias[nombre]["Dispositivos"].append(input(f"Nombre del {i + 1}° dispositivo: "))
        while True:
            try:
                dependencias[nombre]["tipo"].append(int(input("Tipo de dispositivo (1-Electrico/2-Combustible): ")))
            except ValueError:
                print("*****\n*****")
                print ("[!] Error en el dato ingresado\n***Se espera un numero entero")
            else:
                break
    print(dependencias)

def main():
    menu = "\n--- MENÚ ---\n [1] -> Registrar dependencia\n [2] -> Registrar consumo por dependencia\n [3] -> Ver CO2 producido\n [4] -> Dependencia con mayor producción de CO2\n [5] -> Salir\nSelección: "
    dependencias = {}
    while True:
        entrada = input(menu)
        match entrada:
            case "1":
                registrar_dependencia(dependencias)
            case "2":
                registrar_consumo(dependencias)
            case "3":
                print(f"Emisiones totales: {ver_CO2_producido(dependencias)} TCO2")
                os.system("pause")
            case "4":
                depend,co2 = dependencia_con_mayor_produccion_de_CO2(dependencias)
                print(f"La dependencia que mas CO2 emite es {depend} con {co2} TC02")
                print(dependencias)
            case "5":
                break
            case _:
                print("\n[¡] Alerta: Opción inválida.\n")


if __name__ == '__main__':
    main()
