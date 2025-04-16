import csv
from pathlib import Path

def crear_individuo(archivo_individuos):
    """Recibe ubicacion donde crear el archivo maestro de individuos y el Path del detalle para agregar el header"""
    
    detalle_i = Path("archivos") / "usu_individualT324.txt"
    archivo_i = open(archivo_individuos, 'w')
    with open(detalle_i) as archivo:
        csv_reader = csv.reader(archivo)
        header = next(csv_reader)
    for line in header:
        archivo_i.write(line)

    archivo_i.close()

#Creadores de archivos maestros

def crear_hogar(archivo_hogares):
    """Recibe ubicacion donde crear el archivo maestro de hogares y el Path del detalle para agregar el header"""
    detalle_h = Path("archivos") / "usu_hogarT324.txt"
    archivo_h = open(archivo_hogares, "w")
    with open(detalle_h) as archivo:
        csv_reader = csv.reader(archivo)
        header = next(csv_reader)
    for line in header:
        archivo_h.write(line)
    archivo_h.close()