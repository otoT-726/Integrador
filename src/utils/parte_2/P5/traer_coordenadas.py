import json
from src.utils.rutas import data_path

def extraer_coordenadas():
    path_coordenadas = data_path / "aglomerados_coordenadas.json"

    with open(path_coordenadas, "r") as file:
        coordenadas = json.load(file)
    
    return coordenadas
    