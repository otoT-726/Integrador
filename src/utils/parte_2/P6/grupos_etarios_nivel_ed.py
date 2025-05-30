import pandas as pd
import pathlib as pl
from src.utils.rutas import data_path

index_nivel_ed = 'NIVEL_ED'
index_edad = 'CH06'
index_pondera = 'PONDERA'

archivo_individuos = data_path / 'archivo_individuos.txt'

def grupos_etarios(grupo_etarios_seleccionados):
    """
    Recibe un diccionario con los grupos etarios seleccionados como checkbox y devuelve
    un DataFrame con la frecuencia ponderada del nivel educativo más común para cada grupo.
    """
    df = pd.read_csv(archivo_individuos, sep=';', encoding='utf-8')

    def asignar_grupo_etario(edad):
        """Funcion para asignar un grupo etario basado en la edad recibida."""
        for nombre, (min_edad, max_edad) in grupo_etarios_seleccionados.items():
            if min_edad <= edad < max_edad or (max_edad == 120 and edad >= min_edad):
                return nombre
        return None

    #Aplico la función para asignar grupos etarios a la columna de edad del dataframe
    df["grupo_etario"] = df[index_edad].apply(asignar_grupo_etario)
    #Elimino filas donde 'grupo_etario' es None o donde 'NIVEL_ED' es NaN
    df = df.dropna(subset=["grupo_etario", index_nivel_ed])

    # Agrupar y sumar ponderaciones por grupo etario y nivel educativo
    agrupado = df.groupby(["grupo_etario", index_nivel_ed])[index_pondera].sum().reset_index()

    #Ordena el DataFrame por ponderación de mayor a menor y luego agrupa por 'grupo_etario' para obtener el nivel educativo más común
    nivel_mas_comun = agrupado.sort_values(index_pondera, ascending=False).groupby("grupo_etario").first().reset_index()

    # Renombrar columna para claridad del gráfico y para facilitar su uso en el gráfico
    nivel_mas_comun = nivel_mas_comun.rename(columns={index_pondera: "Frecuencia Ponderada"})

    #Devuelve el DataFrame con los grupos etarios y sus frecuencias ponderadas
    return nivel_mas_comun[["grupo_etario", "Frecuencia Ponderada"]].rename(columns={"grupo_etario": "Grupo Etario"})

