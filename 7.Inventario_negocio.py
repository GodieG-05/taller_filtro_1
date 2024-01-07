import os
def calculo_ganancia_potencial(productos:dict):
    header = """
    **************************************
    *   CÁLCULO DE GANANCIA POTENCIAL    *
    **************************************
    """
    print(header)
    ganancia_total = 0
    for clave, valor in productos.items():
        stock_actual = valor["stock actual"]
        valor_venta = valor["valor de venta"]
        valor_compra = valor["valor de compra"]
        ganancia = stock_actual * (valor_venta - valor_compra)
        ganancia_total = ganancia_total + ganancia 
        print(f"Nombre: {valor["Nombre"]}\nStock actual: {valor["stock actual"]}\nRentabilidad por cada {valor["Nombre"]}: {valor_venta - valor_compra}$\nGanancia en {valor["Nombre"]}: {ganancia}$")
        print("*****************************************************************")
    print(f"GANANCIA POTENCIAL TOTAL: {ganancia_total}$")

def informe_produtos_criticos(productos:dict):
    header = """
    **************************************
    *   INFORME DE PRODUCTOS CRÍTICOS    *
    **************************************
    """
    print(header)
    print("Los siguientes productos están por debajo del mínimo de existencias")
    for clave, valor in productos.items():
        stock_actual = valor["stock actual"]
        stock_minimo = valor["stock mínimo"]
        if stock_actual < stock_minimo:
            print("*****************************************************************")
            print(f"Nombre: {valor["Nombre"]}\nStock actual: {valor["stock actual"]}\nStock Mínimo: {valor["stock mínimo"]} ")
        
def actualizacion_producto(productos: dict) -> int:
    header = """
    **************************************
    *     ACTUALIZACIÓN DE PRODUCTOS     *
    **************************************
    """
    print(header)
    codigo = input("Ingrese el código del producto: ")
    for item in productos:
        if codigo in item:
            opciones = "[1] -> Registrar productos adquiridos\n[2] -> Registrar productos vendidos\n Selección: "
            entrada = input(opciones)
            if entrada == "1":
                while True:
                    try:
                        producto_adquirido = int(input("Ingrese la cantidad de producto adquirido: "))
                    except ValueError:
                        print("*****\n*****")
                        print ("[!] Error en el dato ingresado\n***Se espera un numero entero")
                    else:
                        break
                stock_actual = productos[codigo].get("stock actual")
                stock_final = producto_adquirido + stock_actual
                stock_maximo = productos[codigo].get("stock máximo")
                productos[codigo].update({"stock actual":stock_final})
                os.system("cls")
                print(f"Nombre: {productos[codigo]["Nombre"]}\nStock actual: {productos[codigo]["stock actual"]}\nStock Máximo: {productos[codigo]["stock máximo"]}\nStock Mínimo: {productos[codigo]["stock mínimo"]} ")
                if stock_final > stock_maximo:
                    print(f"[!] Hay {stock_final - stock_maximo} unidades de {productos[codigo]["Nombre"]} en exceso")
            elif entrada == "2":
                while True:
                    try:
                        producto_vendido = int(input("Ingrese la cantidad de producto vendido: "))
                    except ValueError:
                        print("*****\n*****")
                        print ("[!] Error en el dato ingresado\n***Se espera un numero entero")
                    else:
                        break
                stock_actual = productos[codigo].get("stock actual")
                stock_final = stock_actual - producto_vendido
                stock_minimo = productos[codigo].get("stock mínimo")
                productos[codigo].update({"stock actual":stock_final})
                print(f"Nombre: {productos[codigo]["Nombre"]}\nStock actual: {productos[codigo]["stock actual"]}\nStock Máximo: {productos[codigo]["stock máximo"]}\nStock Mínimo: {productos[codigo]["stock mínimo"]} ")
                if stock_final < stock_minimo:
                    print(f"[!] Hay {stock_minimo - stock_final} unidades de {productos[codigo]["Nombre"]} en escacez")
def visualizar_productos(productos: dict) -> None:
    header = """
    **************************************
    *   LISTA DE PRODUCTOS REGISTRADOS   *
    **************************************
    """
    for clave,valor in productos.items():
        os.system("cls")
        print(header)
        print(f"Código: {productos[clave]["Codigo"]}\nNombre: {productos[clave]["Nombre"]}\nValor de compra: ${productos[clave]["valor de compra"]}\nValor de venta: ${productos[clave]["valor de venta"]}\nStock Mínimo: {productos[clave]["stock mínimo"]}\nStock Máximo: {productos[clave]["stock máximo"]}\nStock actual: {productos[clave]["stock actual"]}\nNombre de proveedor: {productos[clave]["Nombre de proveedor"]}\n")
        

def registrar_producto(productos: dict) -> None:
    header = """
    **************************************
    *       REGISTRO DE PRODUCTOS        *
    **************************************
    """
    print(header)
    rta = "S"
    while rta in ["S","s"]:
        codigo = (input("Ingrese el código del producto: "))
        productos[codigo]= {"Codigo":codigo,"Nombre": "", "valor de compra": 0, "valor de venta": 0, "stock mínimo": 0, "stock máximo":0, "stock actual":0, "Nombre de proveedor":""}
        productos[codigo].update({"Nombre":input("Ingrese el nombre del producto: ")})
        while True:
            try:
                productos[codigo].update({"valor de compra":float(input("Ingrese el valor de compra del producto: "))})
            except ValueError:
                print("*****\n*****")
                print ("[!] Error en el dato ingresado\n***Se espera un numero entero o decimal")
            else:
                break
        while True:
            try:
                productos[codigo].update({"valor de venta":float(input("Ingrese el valor de venta del producto: "))})
            except ValueError:
                print("*****\n*****")
                print ("[!] Error en el dato ingresado\n***Se espera un numero entero o decimal")
            else:
                break
        while True:
            try:
                productos[codigo].update({"stock mínimo":int(input("Ingrese la cantidad mínima de producto en stock: "))})
            except ValueError:
                print("*****\n*****")
                print ("[!] Error en el dato ingresado\n***Se espera un numero entero")
            else:
                break
        while True:
            try:
                productos[codigo].update({"stock máximo":int(input("Ingrese la cantidad máxima de producto en stock: "))})
            except ValueError:
                print("*****\n*****")
                print ("[!] Error en el dato ingresado\n***Se espera un numero entero")
            else:
                break
        while True:
            try:
                productos[codigo].update({"stock actual":int(input("Ingrese la cantidad actual de producto en stock: "))})
            except ValueError:
                print("*****\n*****")
                print ("[!] Error en el dato ingresado\n***Se espera un numero entero")
            else:
                break
        productos[codigo].update({"Nombre de proveedor":(input("Ingrese el nombre del proveedor del producto: "))})
        rta = input("¿Desea registrar otro producto? Si (s) o No (n)")
        os.system("cls")
    
menu = "\n--- MENÚ ---\n [1] -> Registro de productos\n [2] -> Visualización de productos\n [3] -> Actualización de stock\n [4] -> Informe de productos críticos\n [5] -> Cálculo de ganancia potencial\n [6] -> Salir\n Selección: "
productos = {}
while True:
    entrada = input(menu)
    match entrada:
        case "1":
            registrar_producto(productos)
            os.system("pause")
            os.system("cls")
        case "2":
            visualizar_productos(productos)
            os.system("pause")
            os.system("cls")  
        case "3":
            actualizacion_producto(productos)
            os.system("pause")
            os.system("cls")
        case "4":
            informe_produtos_criticos(productos)
            os.system("pause")
            os.system("cls")
        case "5":
            calculo_ganancia_potencial(productos)
            os.system("pause")
            os.system("cls")
        case "6":
            break
        case _:
            print("\n[¡] Alerta: Opción inválida.\n")