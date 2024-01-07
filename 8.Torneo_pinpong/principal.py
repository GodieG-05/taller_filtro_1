import os

def ver_ganador(torneo_pinpong: dict):
    os.system("cls")
    header = """
    **************************************
    ******       G A N A D O R      ******
    **************************************
    """
    print(header)
    for clave, valor in torneo_pinpong.items():
        total_puntos = 0
        puntos_afavor = 0
        codigo = ""
        nombre = ""
        for item in valor:
            if item["Resultados"][4] > total_puntos:
                total_puntos = item["Resultados"][4]
                puntos_afavor = item["Resultados"][3]
                codigo = item["Código"]
                nombre = item["Nombre"]
            elif item["Resultados"][4] == total_puntos:
                if item["Resultados"][3] > puntos_afavor:
                    puntos_afavor = item["Resultados"][3]
                    total_puntos = item["Resultados"][4]
                    codigo = item["Código"]
                    nombre = item["Nombre"]
                    puntos = item["Resultados"]
        
        print (f"El ganador de la categoria {clave} es el juador {nombre.upper()} con codigo: {codigo} con {total_puntos} PUNTOS y {puntos_afavor} PUNTOS A FAVOR")



def ver_clasificacion(torneo_pinpong: dict):
    os.system("cls")
    header = """
    **************************************
    *            CLASIFICACIÓN           *
    **************************************
    """
    print(header)
    print("Codigo   Jugador   PJ   PG   PP   PAF   PT  ")

    for clave, valor in torneo_pinpong.items():
        for item in valor:
            print(f" {item["Código"]}      {item["Nombre"].upper()}    {item["Resultados"][0]}     {item["Resultados"][1]}    {item["Resultados"][2]}    {item["Resultados"][3]}     {item["Resultados"][4]}")


def registrar_resultado(torneo_pinpong: dict):
    os.system("cls")
    header = """
    **************************************
    *       REGISTRO DE RESULTADOS       *
    **************************************
    """
    print(header)
    for clave, valor in torneo_pinpong.items():
        print(f"Categoria: {clave}")
        for i in range(len(valor)):
            for j in range(i+1,len(valor)):
                print (f"jugador {valor[i]["Nombre"].upper()} con codigo: {valor[i]["Código"]} vs jugador {valor[j]["Nombre"].upper()} con codigo: {valor[j]["Código"]}")
                while True:
                    try:
                        puntos_jugador1 = int(input(f"Ingrese los puntos obtenidos por el jugador con codigo {valor[i]["Código"]}: "))
                    except ValueError:
                                print("*****\n*****")
                                print ("[!] Error en el dato ingresado\n***Se espera un numero entero")
                    else:
                        break
                while True:
                    try:
                        puntos_jugador2 = int(input(f"Ingrese los puntos obtenidos por el jugador {valor[j]["Nombre"]}: "))
                    except ValueError:
                                print("*****\n*****")
                                print ("[!] Error en el dato ingresado\n***Se espera un numero entero")
                    else:
                        break
                valor[i]["Resultados"][0] += 1
                valor[j]["Resultados"][0] += 1 
                if puntos_jugador1 > puntos_jugador2:
                    print(f"El jugador {valor[i]["Nombre"].upper()} ha ganado")
                    valor[i]["Resultados"][1] += 1
                    valor[i]["Resultados"][3] += puntos_jugador1 - puntos_jugador2
                    valor[j]["Resultados"][3] += puntos_jugador2 - puntos_jugador1
                    valor[i]["Resultados"][4] += 2
                    valor[j]["Resultados"][2] += 1
                else:
                    print(f"El jugador {valor[j]["Nombre"].upper()} ha ganado")
                    valor[j]["Resultados"][1] += 1
                    valor[j]["Resultados"][3] += puntos_jugador2 - puntos_jugador1
                    valor[i]["Resultados"][3] += puntos_jugador1 - puntos_jugador2
                    valor[j]["Resultados"][4] += 2
                    valor[i]["Resultados"][2] += 1

                   
def registrar_jugador(torneo_pinpong: dict):
    os.system("cls")
    header = """
    **************************************
    *        REGISTRO DE JUGADORES       *
    **************************************
    """
    print(header)
    rta = "SI"
    print("[¡] EDADES POR CATEGORÍA:\n Novato: 15-16 años\n Intermedio: 17-20 años\n Avanzado: > 20 años")
    os.system("pause")
    os.system("cls")
    while rta.upper() == "SI":
        nombre = input("Ingrese el nombre del jugador: ")
        while True:
            try:
                edad = int(input("Ingrese la edad del jugador: "))
            except ValueError:
                        print("*****\n*****")
                        print ("[!] Error en el dato ingresado\n***Se espera un numero entero")
            else:
                break
    
        codigo = input("Ingrese el código del jugador: ")
        if codigo in torneo_pinpong["Novato"] or codigo in torneo_pinpong["Intermedio"] or codigo in torneo_pinpong["Avanzado"]:
            print("[!] ERROR: Código repetido")
        else:
            if edad == 15 or edad == 16:
                torneo_pinpong["Novato"].append({"Nombre": nombre, "Edad": edad, "Código": codigo, "Resultados": [0,0,0,0,0]})                            
            elif edad > 16 and edad <= 20:
                torneo_pinpong["Intermedio"].append({"Nombre": nombre, "Edad": edad, "Código": codigo, "Resultados": [0,0,0,0,0]})
            elif edad > 20:
                torneo_pinpong["Avanzado"].append({"Nombre": nombre, "Edad": edad, "Código": codigo, "Resultados": [0,0,0,0,0]})
            else: 
                print("[!] ERROR. El jugador no fue registrado. No hay categorías para menores de 15 años")
                os.system("pause") 
        rta = input("¿Desea registrar otro jugador? Si o No: ")
        os.system("cls")
    for clave, valor in torneo_pinpong.items():
        print(f"{clave}:{valor}")

menu = "\n--- MENÚ ---\n [1] -> Registrar Jugador\n [2] -> Registrar resultado\n [3] -> Ver clasificación\n [4] -> Ver ganador\n [5] -> Salir\n Seleccion: "
torneo_pinpong = {
    "Novato": [],
    "Intermedio": [],
    "Avanzado": []
}

while True:
    entrada = input(menu)
    match entrada:
        case "1":
            registrar_jugador(torneo_pinpong)
            os.system("pause")
            os.system("cls")
        case "2":
            registrar_resultado(torneo_pinpong)
            os.system("pause")
            os.system("cls")
        case "3":
            ver_clasificacion(torneo_pinpong)
            os.system("pause")
            os.system("cls")
        case "4":
            ver_ganador(torneo_pinpong)
            os.system("pause")
            os.system("cls")
        case "5":
            break
        case _:
            print("\n[¡] Alerta: Opción inválida.\n")
        