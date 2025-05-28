import pandas as pd
import streamlit as st

from src.utils.rutas import data_path



def mostrar_desocupadas_estudios():
    archivo = data_path / 'archivo_individuos.txt'
    df_individuos = pd.read_csv(archivo, sep = ';')
    
    anos_disponibles = sorted(df_individuos["ANO4"].unique())
    anos = st.selectbox("SELECCIONA UN AÑO QUE DESEE VISUALIZAR", anos_disponibles, index=None, placeholder="Seleccione un año")
    
    trims_disponibles = sorted(df_individuos["TRIMESTRE"].unique())
    trims = st.selectbox("SELECCIONA UN TRIMESTRE", trims_disponibles, index=None, placeholder="Seleccione un trimestre")
    
    filtro = ((df_individuos["ANO4"] == anos) & (df_individuos["TRIMESTRE"] == trims)) 
    
    df_filtrado = df_individuos[filtro]
    
    df_desocupados = df_filtrado[df_filtrado["ESTADO"] == '2']
    
    suma_desocupados = df_filtrado.groupby("NIVEL_ED")["PONDERA"].sum()
    suma_desocupados = suma_desocupados.to_frame()
    
    suma_desocupados = suma_desocupados.rename(columns={"PONDERA" : "total_desocupados"})
    
    total = suma_desocupados["total_desocupados"].sum()
    suma_desocupados["porcentaje"] = (suma_desocupados["total_desocupados"] / total * 100)
    
    st.subheader("Personas desocupadas según nivel educativo")
    st.dataframe(suma_desocupados)