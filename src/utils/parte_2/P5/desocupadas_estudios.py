import pandas as pd
import streamlit as st

from src.utils.rutas import data_path
    
def mostrar_desocupadas_estudios():
    archivo = data_path / 'archivo_individuos.txt'
    df_individuos = pd.read_csv(archivo, sep=';')

    niveles_ed = {
        1 : "Primario incompleto (incluye educación especial)",
        2 : "Primario completo",
        3 : "Secundario incompleto",
        4 : "Secundario completo",
        5 : "Superior universitario incompleto",
        6 : "Superior universitario completo",
        7 : "Sin instrucción",
        9 : "Ns/Nr"
    }

    df_individuos["NIVEL_ED"] = df_individuos["NIVEL_ED"].map(niveles_ed)

    anos_disponibles = sorted(df_individuos["ANO4"].unique())
    anos = st.selectbox("SELECCIONA UN AÑO QUE DESEE VISUALIZAR", anos_disponibles, index=None, placeholder="Seleccione un año")
         
    if (anos!=None):
        # Filtramos solo por el año seleccionado
        df_por_ano = df_individuos[df_individuos["ANO4"] == anos]
        trims_disponibles = sorted(df_por_ano["TRIMESTRE"].unique())
        
        trims = st.selectbox("SELECCIONA UN TRIMESTRE", trims_disponibles, index=None, placeholder="Seleccione un trimestre")

        # Continuar solo si también se seleccionó un trimestre
        if (trims != None):
            filtro = (df_individuos["ANO4"] == anos) & (df_individuos["TRIMESTRE"] == trims)
            df_filtrado = df_individuos[filtro]
            
            df_desocupados = df_filtrado[df_filtrado["ESTADO"] == 2]
            
            suma_desocupados = df_desocupados.groupby("NIVEL_ED")["PONDERA"].sum().to_frame()
            
            suma_desocupados = suma_desocupados.rename(columns={"PONDERA": "Total Desocupados"})
            
            suma_desocupados = suma_desocupados.rename_axis("Nivel Educativo", axis=0)
            
            total = suma_desocupados["Total Desocupados"].sum()
            suma_desocupados["Porcentaje"] = (suma_desocupados["Total Desocupados"] / total * 100)
            
            st.subheader("Personas desocupadas según nivel educativo")
            st.dataframe(suma_desocupados)
