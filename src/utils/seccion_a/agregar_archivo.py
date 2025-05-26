import csv
#EJERCICIO 2 SECCION A
from utils.rutas import project_path, data_path
from utils.seccion_a.agregar_columna_nombres import addColumna #EJERCICIO 3
from utils.seccion_a.agregar_columna_nivelED import addNivelED #EJERCICIO 4
from utils.seccion_a.condicion_laboral import agregar_condicion_laboral #EJERCICIO 5
from utils.seccion_a.columna_tipocasa import columna_tipo_de_casa #EJERCICIO 7
from utils.seccion_a.columna_universitario import columna_universitario_numerica #EJERCICIO 6
from utils.seccion_a.material_tech import agregar_material_techumbre_y_densidad #EJERCICIO 8 y 9 
from utils.seccion_a.condicion_habitabilidad import condicion_de_habitabilidad #EJERCICIO 10

def agregar_trimestre(maestro, detalle):
    """Agrega los datos de un trimestre de eph a nuestra base de datos"""
    with open(detalle, newline="") as archivo:
        csv_reader = csv.reader(archivo, delimiter= ";")
        salteo= next(csv_reader)
        with open(maestro, "a", newline= "") as archivo:
            csv_writer = csv.writer(archivo, delimiter=";")
            for line in csv_reader:
                csv_writer.writerow(line)


def agregar_trimestre_completo_individuo(detalle, maestro = data_path / "archivo_individuos.txt"):
    """Agrega las columnas necesarias al archivo detalle individuo recibido para agregarlo al maestro"""
    addColumna(detalle) #punto 3
    addNivelED(detalle) #punto 4
    agregar_condicion_laboral(detalle) #punto 5
    columna_universitario_numerica(detalle) #punto 6
    #columna_tipo_de_casa(detalle) #punto 7
    #agregar_material_techumbre_y_densidad(detalle) #punto 8 y 9
    #condicion_de_habitabilidad(detalle) #punto 10
    agregar_trimestre(maestro, detalle)


def agregar_trimestre_completo_hogar(detalle, maestro = data_path / "archivo_hogares.txt"):
    """Agrega las columnas necesarias al archivo detalle hogar recibido para agregarlo al maestro"""
    #addColumna(detalle) #punto 3
    #addNivelED(detalle) #punto 4
    #agregar_condicion_laboral(detalle) #punto 5
    #columna_universitario_numerica(detalle) #punto 6
    columna_tipo_de_casa(detalle) #punto 7
    agregar_material_techumbre_y_densidad(detalle) #punto 8 y 9
    condicion_de_habitabilidad(detalle) #punto 10
    agregar_trimestre(maestro, detalle)