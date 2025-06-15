import pandas as pd
from src.utils import diccionario_aglomerados

def calcular_porcentajes(data):
    """Esta función suplementaria para el punto 1.4.7 devuelve una Serie que contiene el aglomerado y
    el porcentaje de viviendas de cada tipo con respecto a la condicion de habitabilidad"""

    total = data['PONDERA'].sum()
    buena = data.loc[data['CONDICION_DE_HABITABILIDAD'] == "Buena", 'PONDERA'].sum() / total * 100
    saludable = data.loc[data['CONDICION_DE_HABITABILIDAD'] == "Saludable", 'PONDERA'].sum() / total * 100
    regular = data.loc[data['CONDICION_DE_HABITABILIDAD'] == "Regular", 'PONDERA'].sum() / total * 100
    mala = data.loc[data['CONDICION_DE_HABITABILIDAD'] == "Insuficiente", 'PONDERA'].sum() / total * 100

    return pd.Series({
        '% Optimas': round(buena, 2),
        '% Saludables': round(saludable, 2),
        '% Regulares': round(regular, 2),
        '% Insuficientes': round(mala, 2)
    
    })

def retornar_informacion_habitabilidad(data: pd.DataFrame):
    """Retorna el dataframe con el porcentaje de casas respecto a 
        condicion de habitabilidad por aglomerado."""
    
    #Toma si es villa o no: 1=si, 2=no 
    resultado = data.groupby('AGLOMERADO').apply(calcular_porcentajes)
    resultado = resultado.rename(index = diccionario_aglomerados)
    

    return resultado