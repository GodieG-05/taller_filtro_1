import os
import registrar_ciudad as ciudad
import registrar_sismo as sismo
import buscar_sismos as buscar
import informe_riesgos as riesgos


menu = "---MENÚ---\n [1] -> Registrar ciudad\n [2] -> Registrar sismo\n [3] -> Buscar sismos por ciudad\n [4] -> Informe de sismos\n [5] -> Salir\nSeleccion: "
ciudades = []
while True:
    entrada = input(menu)
    match entrada:
        case "1":
            ciudad.registrar_ciudad(ciudades)
            os.system("pause")
            os.system("cls")
        case "2":
            sismo.registrar_sismo(ciudades)
            os.system("pause")
            os.system("cls")
        case "3":
            buscar.buscar_sismos_por_ciudad(ciudades)
            os.system("pause")
            os.system("cls")
        case "4":
            riesgos.informe_riesgos(ciudades)
            os.system("pause")
            os.system("cls")
        case "5":
            break
        case _:
            print("\n[¡] Alerta: Opción inválida.\n")
            os.system("pause")
            os.system("cls")