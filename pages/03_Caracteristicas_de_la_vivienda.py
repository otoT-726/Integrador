import sys

import streamlit as st
import pandas as pd
import matplotlib as plt
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


    cantidad_viviendas = cant_viviendas_por_año(archivo_hogares, año)

with tab2:
    
    
    #Esta linea la uso por pura estetica. 
    # No estoy seguro si es la mejor manera de hacerlo
    info = "" if año == None else "en el año " + str(año)
    
    st.header("Cantidad total de viviendas analizadas" + info + ": " + str(cantidad_viviendas))
    st.divider
    st.subheader("Proporción de viviendas segun su tipo.")

    conteo_tipos = archivo_hogares["IV1"]

    #Para crear el pie chart(Grafico de torta)

    conteo_tipos = archivo_hogares[(archivo_hogares["IV1"] <= 6)]["IV1"].value_counts().copy()
    print(conteo_tipos)
    index_list = ["casa", "departamento", "pieza de inquilinato", "pieza de hotel/ pension", "local no construido para habitacion", "otros"]
    conteo_tipos.index = index_list
    conteo_tipos.plot(kind='pie', autopct='%1.1f%%', title='Proporción de viviendas por tipo')

    plt.show()