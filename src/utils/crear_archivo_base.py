import csv
from src.utils.rutas import data_path

def crear_individuo(archivo_individuos):
    """Recibe ubicacion donde crear el archivo maestro de individuos y el Path del detalle para agregar el header"""
    
    detalle_i = data_path / "usu_individual_T324.txt"
    
    with open(detalle_i) as archivo:
        csv_reader = csv.reader(archivo, delimiter=";")
        header = next(csv_reader)
    header.append("CH04str")
    header.append("NIVEL_ED_str")
    header.append("CONDICION_LABORAL")
    header.append("UNIVERSITARIO")
    with open(archivo_individuos, "w", newline="") as archivo:
        csv_writer = csv.writer(archivo, delimiter=";")
        csv_writer.writerow(header)

#Creadores de archivos maestros

def crear_hogar(archivo_hogares):
    """Recibe ubicacion donde crear el archivo maestro de hogares y el Path del detalle para agregar el header"""
    detalle_h = data_path / "usu_hogar_T324.txt"
    with open(detalle_h) as archivo:
        csv_reader = csv.reader(archivo, delimiter=";")
        header= next(csv_reader)
    header.append("TIPO_HOGAR")
    header.append("MATERIAL_TECHUMBRE")
    header.append("DENSIDAD_HOGAR")
    header.append("CONDICION_DE_HABITABILIDAD")
    with open(archivo_hogares, "w", newline="") as archivo:
        csv_writer = csv.writer(archivo, delimiter=";")
        csv_writer.writerow(header)