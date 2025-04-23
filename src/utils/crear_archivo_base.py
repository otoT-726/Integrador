import csv
from pathlib import Path

def crear_individuo(archivo_individuos):
    """Recibe ubicacion donde crear el archivo maestro de individuos y el Path del detalle para agregar el header"""
    
    detalle_i = Path("archivos") / "usu_individual_T324.txt"
    
    with open(detalle_i) as archivo:
        csv_reader = csv.reader(archivo, delimiter=";")
        header = next(csv_reader)
    with open(archivo_individuos, "w", newline="") as archivo:
        csv_writer = csv.writer(archivo, delimiter=";")
        csv_writer.writerow(header)

#Creadores de archivos maestros

def crear_hogar(archivo_hogares):
    """Recibe ubicacion donde crear el archivo maestro de hogares y el Path del detalle para agregar el header"""
    detalle_h = Path("archivos") / "usu_hogar_T324.txt"
    archivo_h = open(archivo_hogares, "w")
    with open(detalle_h) as archivo:
        csv_reader = csv.reader(archivo, delimiter=";")
        header= next(csv_reader)
    with open(archivo_hogares, "w", newline="") as archivo:
        csv.writer(archivo, delimiter=";").writerow(header)