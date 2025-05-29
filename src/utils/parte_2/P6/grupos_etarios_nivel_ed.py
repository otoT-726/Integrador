import pandas as pd
import pathlib as pl
from src.utils.rutas import data_path

index_nivel_ed = 'NIVEL_ED'
index_edad = 'CH06'
index_pondera = 'PONDERA'

archivo_individuos = data_path / 'archivo_individuos.txt'

def grupos_etarios(grupo_etarios_seleccionados):
    """
    Recibe un diccionario con los grupos etarios seleccionados y devuelve
    un DataFrame con la frecuencia ponderada del nivel educativo más común para cada grupo.
    """
    df = pd.read_csv(archivo_individuos, sep=';', encoding='utf-8')

    # Crear la columna 'grupo_etario'
    def asignar_grupo_etario(edad):
        for nombre, (min_edad, max_edad) in grupo_etarios_seleccionados.items():
            if min_edad <= edad < max_edad or (max_edad == 120 and edad >= min_edad):
                return nombre
        return None

    df["grupo_etario"] = df[index_edad].apply(asignar_grupo_etario)
    df = df.dropna(subset=["grupo_etario", index_nivel_ed])

    # Agrupar y sumar ponderaciones
    agrupado = df.groupby(["grupo_etario", index_nivel_ed])[index_pondera].sum().reset_index()

    # Obtener el NIVEL_ED más frecuente para cada grupo
    nivel_mas_comun = agrupado.sort_values(index_pondera, ascending=False).groupby("grupo_etario").first().reset_index()

    # Renombrar columna para claridad
    nivel_mas_comun = nivel_mas_comun.rename(columns={index_pondera: "Frecuencia Ponderada"})

    return nivel_mas_comun[["grupo_etario", "Frecuencia Ponderada"]].rename(columns={"grupo_etario": "Grupo Etario"})

