import pandas as pd
from src.utils import diccionario_aglomerados

def calcular_porcentajes(data):
    """Esta función suplementaria para el punto 1.4.6 devuelve una Serie que contiene el aglomerado,
    la cantidad de viviendas que se ubican en villas de emergencia y el porcentaje con respecto al  total"""

    total = data['PONDERA'].sum()
    pertenece = data.loc[data['IV12_3'] == 1, 'PONDERA'].sum() / total * 100
    return pd.Series({
        'Casas en villa emergencia': data.loc[data['IV12_3'] == 1, 'PONDERA'].sum(),
        '% Casas ubicadas en villas de emergencia': round(pertenece, 2)
    })

def retornar_informacion_villas(data: pd.DataFrame):
    """Retorna el dataframe con el porcentaje de casas en villas emergencia por aglomerado."""
    
    #Toma si es villa o no: 1=si, 2=no 
    data = data[data["IV12_3"].isin([1,2])]
    resultado = data.groupby('AGLOMERADO').apply(calcular_porcentajes)
    resultado = resultado.rename(index = diccionario_aglomerados)
    
    #Ordeno los datos por cantidad de viviendas ubicadas en villas de emergencia
    resultado = resultado.sort_values(by='Casas en villa emergencia', ascending=False)
    
    return resultado