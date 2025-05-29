import streamlit as st
import pandas as pd
from pathlib import Path
from src.utils.rutas import data_path
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from src.utils.parte_2.P6.informar_cantidad_nivel_educativo import informar_cantidad_nivelEd 
from src.utils.parte_2.P6.grupos_etarios_nivel_ed import grupos_etarios
from src.utils.seccion_b.ranking_5_aglomerados import rankin 
#Archivo individuos
archivo_individuos = data_path / "archivo_individuos.txt"
archivo_hogares = data_path / "archivo_hogares.txt"

anio = st.number_input("Ingrese el año para el cual desea ver la cantidad de personas por nivel educativo:", min_value=2023, max_value=2024)

if st.button("Grafico personas por nivel educativo"):
    fig = informar_cantidad_nivelEd(anio)
    if fig:
        st.pyplot(fig)
    else:
        st.warning(f"No hay datos disponibles para el año {anio}.")

st.divider()

# Definí los grupos etarios posibles
todos_los_grupos = {
    "20-30": (20, 30),
    "30-40": (30, 40),
    "40-50": (40, 50),
    "50-60": (50, 60),
    "60+": (60, 120),
}

# Título
st.title("Nivel Educativo Más Común por Grupo Etario")

# Checkboxes para seleccionar grupos
st.subheader("Seleccioná los grupos etarios que querés analizar:")

# Crear checkboxes para cada grupo etario y los almacena en un diccionario con 
# valores booleanos por defecto en True
grupo_seleccionados = {
    k: v for k, v in todos_los_grupos.items() if st.checkbox(k, value=True)
}

# Procesar y mostrar gráfico si hay selección

# ...

if grupo_seleccionados:
    df_resultado = grupos_etarios(grupo_seleccionados)

    if not df_resultado.empty:
        # Ordenar por grupo etario para que el gráfico sea más claro
        df_resultado = df_resultado.sort_values("Grupo Etario")

        # Crear gráfico con matplotlib
        fig, ax = plt.subplots(figsize=(6, 4))  # determino el ancho=6, alto=4 en pulgadas

        #Creamos el gráfico de barras con las frecuencias ponderadas por grupo etario y nivel educativo 
        ax.bar(df_resultado["Grupo Etario"], df_resultado["Frecuencia Ponderada"], color="skyblue")

        # Agregar etiquetas encima de cada barra
        for indice, valor in enumerate(df_resultado["Frecuencia Ponderada"]):
            ax.text(indice, valor, f"{int(valor):,}", ha='center', va='bottom') 

        # enumerate() da el índice y el valor.

        # ax.text(...) ubica el texto en la posición x = indice, y = valor.

        # f"{int(valor):,}" convierte el número a entero con separadores de miles (por ejemplo, 12,345).

        # ha='center': alinea el texto horizontalmente al centro.

        # va='bottom': alinea el texto justo encima de la barra


        #Defino las etiquetas y título del gráfico para el usuario
        ax.set_title("Grafico de los Niveles Educativos más comúnes por grupo Etario")
        ax.set_xlabel("Grupo Etario")
        ax.set_ylabel("Personas (ponderadas)")

        # Muestro el grafico en Streamlit
        st.pyplot(fig)

    else:
        st.info("No hay datos para los grupos seleccionados.")
else:
    st.warning("Seleccioná al menos un grupo para ver el gráfico.")

st.divider()

st.subheader("Ranking de los 5 Aglomerados con mayor porcentaje de hogares con individuos con estudios universitarios o superiores finalizados") 

#boton para exportar el ranking de los 5 aglomerados a un archivo CSV

exportar = st.button("Exportar Ranking a CSV")


if exportar:
    df_ranking = rankin(archivo_individuos, archivo_hogares)
    df_ranking.index = df_ranking.index + 1 #Ajusto el índice para que empiece en 1 

    if not df_ranking.empty:
        st.write("Resultado del ranking:")
        st.dataframe(df_ranking)

        # Convertir a CSV y ofrecer descarga
        csv_data = df_ranking.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Descargar CSV",
            data=csv_data,
            file_name="ranking_aglomerados.csv",
            mime="text/csv"
        )
    else:
        st.info("No se encontraron datos para calcular el ranking.")