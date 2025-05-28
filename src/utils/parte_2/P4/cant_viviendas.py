import pandas as pd
from src.utils.rutas import data_path

def cant_viviendas_por_año(data, año):
    if año == None:
        return data["PONDERA"].sum()
    else:
        mask = (data["ANO4"] == año)
        return data[mask]["PONDERA"].sum()
    