from pathlib import Path
from src.utils.agregar_archivo import agregar_trimestre
from src.utils.crear_archivo_base import crear_hogar, crear_individuo
from src.utils.rutas import project_path, data_path
from src.utils.AgregarColumnaNombres import addColumna
from src.utils.AgregarColumnaNivelED import addNivelED
from src.utils.condicion_laboral import agregar_condicion_laboral
from src.utils.columna_tipocasa import columna_tipo_de_casa
from src.utils.columna_universitario import columna_universitario_numerica

#Path configurable de detalle para agregar archivos al maestro

detalle_i = data_path / "usu_individual_T24.txt"
detalle_h = data_path / "usu_hogar_T24.txt"

#Path maestros
archivo_individuos = data_path / "archivo_individuos.txt"
archivo_hogares = data_path / "archivo_hogares.txt"



"""crear_individuo(archivo_individuos)"""

#Creadores de archivos maestros

"""crear_hogar(archivo_hogares)"""

try:
    agregar_trimestre(archivo_individuos, detalle_i)
except FileNotFoundError:
    print('El archivo que estás intentando agregar no existe o no se encuentra en la carpeta correspondiente')


# Seccion a:
#addColumna(archivo_individuos) punto 3
#addNivelED(archivo_individuos) punto 4

#agregar_condicion_laboral(archivo_individuos) #punto 5
#agregar_condicion_laboral(archivo_hogares) #punto 5
#columna_universitario_numerica(archivo_individuos) #punto 6
#columna_tipo_de_casa(archivo_hogares) #punto 7