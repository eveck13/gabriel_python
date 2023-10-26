# Importa las bibliotecas necesarias
import json
import yaml
import xml.etree.ElementTree as ET
# Crea una lista vacía para almacenar la información de las personas
personas = []

# Solicita al usuario la información de cada persona
for i in range(10):
    nombre = input("Ingrese el nombre de la persona {}: ".format(i + 1))
    matricula = input("Ingrese la matrícula de la persona {}: ".format(i + 1))
    especialidad = input("Ingrese la especialidad de la persona {}: ".format(i + 1))

    # Crea un objeto persona con la información proporcionada
    persona = {
        "nombre": nombre,
        "matrícula": matricula,
        "especialidad": especialidad
    }

    # Agrega la persona a la lista
    personas.append(persona)