import pandas as pd
from src.utils import diccionario_aglomerados

def calcular_porcentajes(data):
    """Esta función suplementaria para el punto 1.4.4 devuelve una Serie que contiene el aglomerado,
    el porcentaje de viviendas que tienen baños interiores, y porcentaje de las viviendas que no"""

    total = data['PONDERA'].sum()
    primer_material = data.loc[data['IV8'] == 1, 'PONDERA'].sum() / total * 100
    segundo_material = data.loc[data['IV8'] == 2, 'PONDERA'].sum() / total * 100
    return pd.Series({
        '% Con baños interiores': round(primer_material, 2),
        '% Sin baños interiores': round(segundo_material, 2),
    })

def retornar_informacion_baños(data):
    """Retorna el dataframe con el porcentaje de tenencia de baños por aglomerado."""
    
    #Toma todos los que tienen baño (1) y los que no (2)
    data = data[data["IV8"].isin([1,2])]
    resultado = data.groupby('AGLOMERADO').apply(calcular_porcentajes)
    resultado = resultado.rename(index = diccionario_aglomerados)
    
    return resultado