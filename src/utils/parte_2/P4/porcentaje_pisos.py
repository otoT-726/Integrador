import pandas as pd
from src.utils import diccionario_aglomerados

def calcular_porcentajes(data):
    """Esta función suplementaria para el punto 1.4.3 devuelve una Serie que contiene el aglomerado,
    el porcentaje de viviendas que tienen pisos de mejores condiciones, porcentaje de viviendas que tienen
    pisos de condiciones regulares, y porcentaje de viviendas sin piso o que no satisfacen las necesidades
    de habitabilidad"""

    total = data['PONDERA'].sum()
    primer_material = data.loc[data['IV3'] == 1, 'PONDERA'].sum() / total * 100
    segundo_material = data.loc[data['IV3'] == 2, 'PONDERA'].sum() / total * 100
    tercer_material = data.loc[data['IV3'] == 3, 'PONDERA'].sum() / total * 100
    return pd.Series({
        '% Pisos de óptima calidad': round(primer_material, 2),
        '% Cemento/ Ladrillo fijo': round(segundo_material, 2),
        '% Tierra/ Ladrillo suelto': round(tercer_material, 2)
    })

def retornar_informacion_pisos(data):
    """Retorna el dataframe con el porcentaje de tipo de pisos por aglomerado."""
    
    #Toma tipos de piso: 1, 2 y 3
    data = data[data["IV3"].isin([1,2,3])]
    resultado = data.groupby('AGLOMERADO').apply(calcular_porcentajes)
    resultado = resultado.rename(index = diccionario_aglomerados)
    
    return resultado