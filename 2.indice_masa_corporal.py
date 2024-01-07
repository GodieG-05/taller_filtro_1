import os
print(""" 
BIENVENIDO A SU PORTAL DE BIENESTAR ESTUDIANTIL
++ Estado de Forma de Los Estudiantes Basado en el Indice de Masa Corporal (IMC) ++
""")

def verAlumno(alumnos):
    for key,valor in alumnos.items():
        print(f"{key}: {valor}")

rta = "S"
while rta in ["S","s"]:
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = input(f"Ingrese la edad de {nombre}: ")
    while True:
        try:
            altura = float(input(f"Ingrese la altura de {nombre} en metros: "))
        except ValueError:
            os.system("cls")
            print("[!] Error en el dato ingresado")
            print("*** SE ESPERA UN NUMERO ENTERO O DECIMAL")
            os.system("pause")
        else:
            break
    while True:
        try:
            peso = float(input(f"Ingrese el peso de {nombre} en kilogramos: "))
        except ValueError:
            os.system("cls")
            print("[!] Error en el dato ingresado")
            print("*** SE ESPERA UN NUMERO ENTERO O DECIMAL")
            os.system("pause")
        else:
            break
    indiceMasac = peso/altura**2
    imc = round(indiceMasac,2)
    alumnos = {
    "nombre" : nombre,
    "edad" : (f"{edad} años"),
    "peso" : (f"{peso} Kg"),
    "altura" : (f"{altura} m"),
    "IMC" : imc,
    "Estado de forma" : ""
    }
    os.system("cls")
    if (imc < 18.5):
        alumnos["Estado de forma"] = "BAJO PESO"
    elif (imc >= 18.5 and imc <= 24.9):
        alumnos["Estado de forma"] = "PESO IDEAL"
    elif (imc >= 25 and imc <= 29.9):
        alumnos["Estado de forma"] = "SOBREPESO"
    elif (imc >= 30 and imc <= 34.9):
        alumnos["Estado de forma"] = "OBESIDAD I"
    elif (imc >= 35 and imc <= 39.9):
        alumnos["Estado de forma"] = "OBESIDAD II"
    elif (imc >40):
        alumnos["Estado de forma"] = "OBESIDAD III"
    verAlumno(alumnos)

    rta = input("Desea registrar otro Alumno S(si) o N(No)").upper()
    os.system("cls")
