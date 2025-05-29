import sys

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from src.utils import rutas
from src.utils.parte_2.P4.cant_viviendas import cant_viviendas_por_año

sys.path.append(str(Path(__file__).parent.parent / 'src'))

ruta_hogares = rutas.data_path / 'archivo_hogares.txt'
archivo_hogares = pd.read_csv(ruta_hogares, sep=";", low_memory=False)

tab1, tab2 = st.tabs(["Información", "Visualización"])

with tab1:

    st.title("Caracteristicas de la vivienda.")

    st.subheader("En esta sección se visualizará información relacionada a las características de las viviendas de la población argentina según la EPH.")

    #En esta parte se permite seleccionar un año en particular para visualizar
    #sus datos o dejar sin marcar para ver todos los años.

    año = None
   
    #En caso de querer seleccionar un año, creo una tupla con los años contenidos en el dataset.
    #Para estar seguro que los años no sean errores filtro los años que aparezcan mas de 1000(mil) veces.
    conteo_años = archivo_hogares["ANO4"].value_counts()
    años_incluidos = conteo_años[conteo_años > 4000].index
    año = st.selectbox("Presione aquí para ingresar un año", tuple(años_incluidos),index= None, placeholder="Que año quisieras visualizar?")


with tab2:
    
    #Linea necesaria para filtrar los datos en caso de que se haya seleccionado un año
    archivo_hogares = archivo_hogares if año is None else archivo_hogares[archivo_hogares["ANO4"] == año]
    #Esta linea la uso por pura estetica. 
    # No estoy seguro si es la mejor manera de hacerlo
    info = "" if año == None else "en el año " + str(año)
    
    st.header("Cantidad total de viviendas analizadas" + info + ": " + str(archivo_hogares["PONDERA"].sum()))
    

    st.divider()
    
    st.subheader("Proporción de viviendas segun su tipo.")
    

    #Para crear el pie chart(Grafico de torta)
    

    conteo = archivo_hogares[archivo_hogares["IV1"] <= 6].groupby("IV1")["PONDERA"].sum()
    
    
    #Creo las categorias del gráfico
    casa = conteo.get(1, 0)
    departamento = conteo.get(2, 0)
    otros = conteo.loc[3:6].sum()
    
    #Creo las series con los datos
    conteo_tipos = [casa, departamento, otros]
    index_list = ["casa", "departamento", "otros"]
    
    #Creo el gráfico
    fig, ax = plt.subplots()
    ax.pie(conteo_tipos, labels=index_list, autopct='%1.1f%%')
    ax.set_title('Proporción de viviendas por tipo')
    ax.axis('equal') 
    st.pyplot(fig)


    st.subheader("OTROS:")

    total_ponderado = archivo_hogares[archivo_hogares["IV1"] <= 6]["PONDERA"].sum()
    
    #Uso estos calculos para devolver el porcentaje que representan los tipos de vivienda que componen "OTROS"
    #(cant_elementos / total_ponderado) * 100
    st.write(f"pieza de inquilinato: {((archivo_hogares[archivo_hogares['IV1'] == 3]["PONDERA"].sum()) / total_ponderado)*100:0.2}%")
    st.write(f"pieza de hotel/pensión: {((archivo_hogares[archivo_hogares['IV1'] == 4]["PONDERA"].sum()) / total_ponderado)*100:0.2}%")
    st.write(f"local no construido para habitación: {((archivo_hogares[archivo_hogares['IV1'] == 5]["PONDERA"].sum()) / total_ponderado)*100:0.2}%")
    
    st.divider()