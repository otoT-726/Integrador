import pandas as pd
def calcular_tasas_por_aglomerado(df_individuos, aniomax, trimmax):
    index_anio = 'ANO4'
    index_trimestre = 'TRIMESTRE'
    filtro = (
        ((df_individuos[index_anio] == aniomax) & (df_individuos[index_trimestre] == trimmax))
    )
    data_filtrada = df_individuos[filtro]
    resultado = []
    agrupado_por_aglomerado = data_filtrada.groupby('AGLOMERADO')

    for aglomerado, grupo in agrupado_por_aglomerado:
        poblacion_total = grupo['PONDERA'].sum()
        ocupados = grupo[grupo['ESTADO'] == 1]['PONDERA'].sum()
        desocupados = grupo[grupo['ESTADO'] == 2]['PONDERA'].sum()

        activos = ocupados + desocupados

        tasa_empleo = (ocupados / poblacion_total) * 100 if poblacion_total > 0 else 0
        tasa_desempleo = (desocupados / activos) * 100 if activos > 0 else 0

        resultado.append({
            'AGLOMERADO': aglomerado,
            'Tasa Empleo': tasa_empleo,
            'Tasa Desempleo': tasa_desempleo
        })
    return resultado