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
     # Crea un objeto persona con la información proporcionada
    persona = {
        "nombre": nombre,
        "matrícula": matricula,
        "especialidad": especialidad
    }

    # Agrega la persona a la lista
    personas.append(persona)

# Imprime la información en formato JSON
print(json.dumps(personas, indent=4))

# Imprime la información en formato YAML
print(yaml.dump(personas, indent=4))

# Imprime la información en formato XML
root = ET.Element("personas")
for persona in personas:
    persona_node = ET.SubElement(root, "persona")
    for key, value in persona.items():
        ET.SubElement(persona_node, key).text = value
        
xml_string = ET.tostring(root, encoding="utf-8")
print(xml_string)