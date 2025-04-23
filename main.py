from pathlib import Path
from src.utils.agregar_archivo import agregar_trimestre
from src.utils.crear_archivo_base import crear_hogar, crear_individuo

#Path configurable de detalle para agregar archivos al maestro

detalle_i = Path("archivos") / "usu_individual_T24.txt"
detalle_h = Path("archivos") / "usu_hogar_T324.txt"

#Path maestros
archivo_individuos = Path("archivos") / "archivo_individuos.txt"
archivo_hogares = Path("archivos") / "archivo_hogares.txt"



"""crear_individuo(archivo_individuos)"""

#Creadores de archivos maestros

crear_hogar(archivo_hogares)

try:
    agregar_trimestre(archivo_hogares, detalle_h)
except FileNotFoundError:
    print('El archivo que estás intentando agregar no existe o no se encuentra en la carpeta correspondiente')