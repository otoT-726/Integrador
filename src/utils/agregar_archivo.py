import csv
from src.utils.rutas import project_path, data_path
from src.utils.AgregarColumnaNombres import addColumna
from src.utils.AgregarColumnaNivelED import addNivelED
from src.utils.condicion_laboral import agregar_condicion_laboral
from src.utils.columna_tipocasa import columna_tipo_de_casa
from src.utils.columna_universitario import columna_universitario_numerica
from src.utils.materialTech import agregar_material_techumbre_y_densidad
from src.utils.condicion_habitabilidad import condicion_de_habitabilidad 

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
    addColumna(detalle) #punto 3
    addNivelED(detalle) #punto 4
    agregar_condicion_laboral(detalle) #punto 5
    columna_universitario_numerica(detalle) #punto 6
    #columna_tipo_de_casa(detalle) #punto 7
    #agregar_material_techumbre_y_densidad(detalle) #punto 8 y 9
    #condicion_de_habitabilidad(detalle) #punto 10
    agregar_trimestre(maestro, detalle)


def agregar_trimestre_completo_hogar(detalle, maestro = data_path / "archivo_hogares.txt"):
    #addColumna(detalle) #punto 3
    #addNivelED(detalle) #punto 4
    #agregar_condicion_laboral(detalle) #punto 5
    #columna_universitario_numerica(detalle) #punto 6
    columna_tipo_de_casa(detalle) #punto 7
    agregar_material_techumbre_y_densidad(detalle) #punto 8 y 9
    condicion_de_habitabilidad(detalle) #punto 10
    agregar_trimestre(maestro, detalle)