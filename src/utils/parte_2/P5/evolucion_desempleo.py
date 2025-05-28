import pandas as pd
from src.utils.rutas import data_path

detalle_individuos = data_path / "archivo_individuos.txt"

def data_frame_empleo(aglomerado=None):
    df = pd.read_csv(detalle_individuos, sep=";")
    
    if aglomerado is not None:
        df = df[df["AGLOMERADO"] == aglomerado]

    df["PERIODO"] = df["ANO4"].astype(str) + "T" + df["TRIMESTRE"].astype(str)

    def calcular_tasas(grupo):
        ocupados = grupo[grupo["ESTADO"] == 1]["PONDERA"].sum()
        desocupados = grupo[grupo["ESTADO"] == 2]["PONDERA"].sum()
        total = ocupados + desocupados
        tasa_empleo = (ocupados / total * 100) if total > 0 else 0
        tasa_desempleo = (desocupados / total * 100) if total > 0 else 0
        return pd.Series({
            "tasa_empleo": tasa_empleo,
            "tasa_desempleo": tasa_desempleo
        })

    tasas = df.groupby("PERIODO").apply(calcular_tasas).reset_index()
    return tasas

