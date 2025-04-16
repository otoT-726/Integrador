from pathlib import Path
from src.funciones.agregar_archivo import agregar_trimestre
from src.funciones.crear_archivo_base import crear_hogar, crear_individuo

#Path configurable de detalle para agregar archivos al maestro

detalle_i = Path("archivos") / "usu_individual_T124.txt"
detalle_h = Path("archivos") / "usu_hogar_T124.txt"

#Path maestros
archivo_individuos = Path("archivos") / "archivo_individuos.txt"
archivo_hogares = Path("archivos") / "archivo_hogares.txt"



"""crear_individuo(archivo_individuos)"""

#Creadores de archivos maestros

"""crear_hogar(archivo_hogares)"""


agregar_trimestre(archivo_individuos, detalle_i)
