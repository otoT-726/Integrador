import pandas as pd
from src.utils import diccionario_aglomerados

def calcular_porcentajes(data):
    """Esta función suplementaria para el punto 1.5.4 devuelve una Serie que contiene el aglomerado,
    la cantidad de personas con ocupación y el porcentaje de empleados estatales, privados y otros tipos"""

    total = data['PONDERA'].sum()
    estatal = data.loc[data['PP04A'] == 1, 'PONDERA'].sum() / total * 100
    privado = data.loc[data['PP04A'] == 2, 'PONDERA'].sum() / total * 100
    otros = data.loc[data['PP04A'] == 3, 'PONDERA'].sum() / total * 100
    return pd.Series({
        'Individuos con ocupación': data.loc[data['ESTADO'] == 1, 'PONDERA'].sum(),
        '% Trabajadores estatales': round(estatal, 2),
        '% Trabajadores privados': round(privado, 2),
        '% Otros': round(otros, 2)
    })

def retornar_informacion_trabajadores(data: pd.DataFrame):
    """Retorna el dataframe con el porcentaje de empleados estatales, privados y de otros tipos."""
    
    #Filtra los datos con la información del tipo de trabajo: 1=estatal, 2=privado, 3=otros.
    data = data[data["PP04A"].isin([1,2,3])]
    resultado = data.groupby('AGLOMERADO').apply(calcular_porcentajes)
    resultado = resultado.rename(index = diccionario_aglomerados)
    
    #Los ordeno por visualizar los datos de forma más ordenada
    resultado = resultado.sort_values(by='Individuos con ocupación', ascending=False)
    
    return resultado