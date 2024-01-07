import os
import random
print(""" 
BIENVENIDO A SU PORTAL DE BIENESTAR ESTUDIANTIL
estado de forma de los estudiantes basado en el Indice de Masa Corporal (IMC)
""")
alumnos = []
nombres = ["pepito","maria","pedro","alejandro","andrea","adriana","jose","antonio","diego","mariana","sara","tania","felix",]
bajoPeso = 0
normal = 0
sobrepeso = 0
obesidad1 = 0
obesidad2 = 0
obesidad3 = 0
def verAlumno(alumnos):
    for key, valor in enumerate(alumnos):
        print(f"{key}: {valor}\n")
for i in range(20):
    nombre = random.choice(nombres)
    edad = random.randint(16,28)
    altura = round(random.uniform(1.5,2.0),2)
    peso = random.randint(50,100)
    indiceMasac = peso/altura**2
    imc = round(indiceMasac,2)
    alumno = {
    "nombre" : nombre,
    "edad" : (f"{edad} años"),
    "peso" : (f"{peso} Kg"),
    "altura" : (f"{altura} m"),
    "IMC" : imc,
    "Estado de forma" : ""
    }
    os.system("cls")
    if (imc < 18.5):
        alumno["Estado de forma"] = "BAJO PESO"
        bajoPeso = bajoPeso + 1
    elif (imc >= 18.5 and imc <= 24.9):
        alumno["Estado de forma"] = "PESO IDEAL"
        normal = normal + 1
    elif (imc >= 25 and imc <= 29.9):
        alumno["Estado de forma"] = "SOBREPESO"
        sobrepeso = sobrepeso + 1
    elif (imc >= 30 and imc <= 34.9):
        alumno["Estado de forma"] = "OBESIDAD I"
        obesidad1 = obesidad1 + 1
    elif (imc >= 35 and imc <= 39.9):
        alumno["Estado de forma"] = "OBESIDAD II"
        obesidad2 = obesidad2 + 1
    elif (imc >40):
        alumno["Estado de forma"] = "OBESIDAD III"
        obesidad3 = obesidad3 + 1
    alumnos.append(alumno)
    os.system("cls")
verAlumno(alumnos)
os.system("pause")

print(f"{bajoPeso} estudiantes se encuentran bajos de peso")
print(f"{normal} estudiantes se encuentran en el peso ideal")
print(f"{sobrepeso} estudiantes se encuentran en sobrepeso")
print(f"{obesidad1} estudiantes se encuentran en obesidad I")
print(f"{obesidad2} estudiantes se encuentran en obesidad II")
print(f"{obesidad3} estudiantes se encuentran en obesidad III")

