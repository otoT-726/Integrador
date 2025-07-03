from src.utils.rutas import data_path
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from src.utils.rutas import data_path
#1.7 (P7) Ingresos
def debajo_de_lineas():
    #anoto los trimestres, 1, con sus respectivos meses
    #esto es para poder filtrar los datos por trimestre
    #y no por mes, ya que la EPH se realiza trimestralmente
    #y no mensualmente.
    #Los trimestres son:
    #Cargo el archivo de hogares
    arch_hogares = data_path / 'archivo_hogares.txt'
    df_hogares = pd.read_csv(arch_hogares, encoding='utf-8', sep=';')
    
    trimestres = {
        1: (1,2,3),
        2: (4,5,6),
        3: (7,8,9),
        4: (10,11,12)
    }
    ano = st.selectbox("AÑO", df_hogares["ANO4"].unique())
    trimestre = st.selectbox("TRIMESTRE", list(trimestres.keys()))
    mostrar = st.button("Mostrar resultados")
    
    if mostrar:
        
        #filtro los hogares con ITF Y CANTIDAD DE PERSONAS A 4.
        filtro_hogares = (df_hogares["ITF"] > 0) & (df_hogares["IX_TOT"] == 4) & (df_hogares["ANO4"] == ano) & (df_hogares["TRIMESTRE"] == trimestre)
        df_hogares_filtrado = df_hogares[filtro_hogares]
        
        #cargo el archivo de canasta basica
        arch_canasta = data_path / 'valores-canasta-basica-alimentos-canasta-basica-total-mensual-2016.csv'
        df_canasta = pd.read_csv(arch_canasta)

        df_canasta['indice_tiempo'] = pd.to_datetime(df_canasta['indice_tiempo'])
        df_canasta_filtrado = df_canasta[(df_canasta['indice_tiempo'].dt.year == ano) & 
                                        (df_canasta['indice_tiempo'].dt.month.isin(trimestres[trimestre]))]
        
        linea_de_indigencia = df_canasta_filtrado['linea_indigencia'].mean()
        linea_de_pobreza = df_canasta_filtrado['linea_pobreza'].mean()
        
        df_hogares_filtrado["es_indigente"] = df_hogares_filtrado['ITF'] < linea_de_indigencia
        df_hogares_filtrado["es_pobre"] = (df_hogares_filtrado['ITF'] < linea_de_pobreza) & (df_hogares_filtrado['ITF'] > linea_de_indigencia)

        total_hogares = df_hogares_filtrado["PONDERA"].sum()
        total_indigentes = df_hogares_filtrado[df_hogares_filtrado["es_indigente"]]["PONDERA"].sum()
        total_pobres = df_hogares_filtrado[df_hogares_filtrado["es_pobre"]]["PONDERA"].sum()
        porcentaje_indigentes = (total_indigentes / total_hogares) * 100
        porcentaje_pobres = (total_pobres / total_hogares) * 100
        
        st.subheader(f"Resultados para el año {ano} y trimestre {trimestre}")
        col1, col2,col3 = st.columns(3)
        with col1:
            st.write("Total de hogares analizados:", f"{total_hogares:,.0f}")
        with col2:
            st.write("Total de hogares indigentes:", f"{total_indigentes:,.0f} ({porcentaje_indigentes:.2f}%)")
        with col3:
            st.write("Total de hogares pobres:", f"{total_pobres:,.0f} ({porcentaje_pobres:.2f}%)")
        # Grafico de barras
        fig, ax = plt.subplots()
        ax.bar(["Indigentes", "Pobres"], [total_indigentes, total_pobres], color=['red', 'orange'])
        ax.set_ylabel("Cantidad de hogares")
        ax.set_title(f"Hogares indigentes y pobres en {ano} - Trimestre {trimestre}")
        st.pyplot(fig)