import sys

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from src.utils.parte_2.P4.porcentaje_pisos import retornar_informacion_pisos
from src.utils.parte_2.P4.porcentaje_baños import retornar_informacion_baños
from src.utils import rutas
from src.utils import diccionario_aglomerados

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
    
    #Esta linea la uso por pura estetica. No estoy seguro si es la mejor manera de hacerlo
    info = "" if año == None else "en el año " + str(año)
    
    st.header("Cantidad total de viviendas analizadas " + info + ": ")
    st.header(str(archivo_hogares["PONDERA"].sum()))
    st.divider()
    
    st.subheader("Proporción de viviendas segun su tipo.")
    
    #Punto 1.4.2

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
    ax.pie(conteo_tipos, labels=index_list, autopct='%1.1f%%', colors=["#803892", "#2BB39C", "#4087A3"])
    ax.set_title('Proporción de viviendas por tipo')
    ax.axis('equal')
    
    st.pyplot(fig)


    st.subheader("OTROS:")

    
    #Uso estos calculos para devolver el porcentaje que representan los tipos de vivienda que componen "OTROS"
    #(cant_elementos / total_ponderado) * 100
    
    total_ponderado = archivo_hogares[archivo_hogares["IV1"] <= 6]["PONDERA"].sum()

    st.write(f"pieza de inquilinato: {((archivo_hogares[archivo_hogares['IV1'] == 3]["PONDERA"].sum()) / total_ponderado)*100:0.2}%")
    st.write(f"pieza de hotel/pensión: {((archivo_hogares[archivo_hogares['IV1'] == 4]["PONDERA"].sum()) / total_ponderado)*100:0.2}%")
    st.write(f"local no construido para habitación: {((archivo_hogares[archivo_hogares['IV1'] == 5]["PONDERA"].sum()) / total_ponderado)*100:0.2}%")
    
    st.divider()


    #Punto 1.4.3:Se informará, para cada aglomerado, cuál es el material predominante en los pisos interiores de las viviendas.

    st.subheader("PORCENTAJE DE TIPOS DE PISOS POR AGLOMERADO")
    #En este punto había que retornar el tipo de pisos más común por aglomerado.
    #Pero como se ve en los datos, todos los aglomerados retornaban el tipo de piso 1.
    #Por esta cuestión decidí que era mas conveniente retornar directamente el porcentaje

    resultado = retornar_informacion_pisos(archivo_hogares)
    st.write(resultado)


    st.divider()


    #Punto 1.4.4: Se mostrará, por aglomerado, la proporción de viviendas que disponen de baño dentro del hogar en el año seleccionado.

    st.subheader("PORCENTAJE VIVIENDAS CON BAÑO INTERIOR POR AGLOMERADO")
    #Reutilizo el punto anterior para el siguiente:

    resultado = retornar_informacion_baños(archivo_hogares)
    st.write(resultado)

    st.divider()

    #Punto 1.4.5: Además del año seleccionado, se debe ingresar un aglomerado específico. Se mostrará
                # la evolución del régimen de tenencia (propia, alquilada, cedida, etc.) para ese aglomerado.
                # El usuario debe poder elegir el tipo de tenencia que desea ver: una, un conjunto o todas.

    st.subheader("EVOLUCION DEL REGIMEN DE TENENCIA")

    st.write("A continuacion podra elegir un aglomerado para visualizar la evolución del regimen de tenencia de los habitantes sobre sus viviendas.")


    conteo_aglomerados = archivo_hogares["AGLOMERADO"].unique()
    

    #Guardo los nombres de los aglomerados en una lista, para luego permitir seleccionar el aglomerado por nombre.
    nombres_aglomerados = []
    for valor in diccionario_aglomerados.values():
        nombres_aglomerados.append(valor)

    aglomerado_incluido = st.selectbox("Elija que aglomerado desea visualizar:", nombres_aglomerados, index= None, placeholder="SELECCIONE UN AGLOMERADO")

    #aglomerados_incluidos = st.multiselect("Elija los aglomerados que desea visualizar:", nombres_aglomerados, placeholder="TODOS") -> Para poder elegir multiples aglomerados(INCOMPLETO)

    #Creo la lista para elegir el regimen de tenencia por nombre
    lista_tenencia = ["Propietario de la vivienda y el terreno", "Propietario únicamente de la vivienda",
                    "Inquilino", "Ocupante por pago de impuestos", "Ocupante en relacion de dependencia",
                    "Ocupante gratuito", "Ocupante de hecho", "En sucesión"]

    #Filtro los tipos de tenencia en dependencia de lo que seleccione el usuario.
    tenencia_incluida = st.multiselect("Elija el régimen de tenencia que desea visualizar:", lista_tenencia, placeholder="TODOS")
    if not tenencia_incluida:
        tenencia_incluida = lista_tenencia


    #Espero a que ingresen un trimestre para continuar.
    if(aglomerado_incluido == None):
        st.write("Seleccione un aglomerado para visualizar su información")
    else:
        st.subheader(aglomerado_incluido)

        #Creo un diccionario invertido de aglomerados para poder acceder al codigo mediante el nombre. Y creo un diccionario para acceder a los codigos del regimen de vivienda('II7') y viceversa.

        diccionario_aglomerados_invertido = {valor: clave for clave, valor in diccionario_aglomerados.items()}

        diccionario_regimen = {lista_tenencia[i]: i+1 for i in range(0, len(lista_tenencia))}

        diccionario_regimen_invertido = {valor: clave for clave, valor in diccionario_regimen.items()}

        cod_aglomerado = diccionario_aglomerados_invertido[aglomerado_incluido]

        #Uso list-comprehension para recuperar los codigos de tenencia que se incluyen a la visualización. Nótese que tenencia_incluida es una lista y por eso no se puede usar como clave.
        codigos_tenencia = [diccionario_regimen[tenencia] for tenencia in tenencia_incluida]
        mask = (archivo_hogares["AGLOMERADO"] == cod_aglomerado) & (archivo_hogares["II7"].isin(codigos_tenencia))
        
        #Filtro la ponderación de hogares por aglomerado y regimenes seleccionados. Realizo una copia porque voy a agregar mas columnas a este dataframe para graficar.
        filtro = archivo_hogares[mask].copy()
        
        #Agrupo por año, trimestre y regimen seleccionado
        grupo = filtro.groupby(["ANO4", "TRIMESTRE", "II7"])["PONDERA"].sum().reset_index()
        
        #Agrego columna 'PERIODO' para agrupar año y trimestre, y columna 'TENENCIA' para recuperar el nombre del regimen basado en su codigo.
        grupo["PERIODO"] = grupo["ANO4"].astype(str) + "T" + grupo["TRIMESTRE"].astype(str)

        
        grupo["TENENCIA"] = grupo["II7"].map(diccionario_regimen_invertido)

        #Grafico.
        fig, ax = plt.subplots(figsize=(12, 9))
        #Itero por cada uno de los tipos de tenencia y grafico en función de si se encuentran seleccionadas. Ademas voy guardando las etiquetas para luego mostrar cada una por separado.
        for tenencia in grupo["TENENCIA"].unique():
            data = grupo[grupo["TENENCIA"] == tenencia]
            ax.plot(data["PERIODO"], data["PONDERA"], marker='o', label=tenencia)

        ax.set_title(f"EVOLUCION REGIMEN DE TENENCIA")
        ax.set_xlabel("Periodo (Año-Trimestre)")
        ax.set_ylabel("Cantidad de viviendas segun su tipo")
        ax.legend()
        plt.grid()
        plt.xticks(rotation=45)

        st.pyplot(fig)


    st.divider()

    #Punto 1.4.6:  Informar de manera ordenada (decreciente) la cantidad de viviendas ubicadas en villa 
                # de emergencia por aglomerado. Además de la cantidad informar el porcentaje con respecto al total.

    #Columna 'IV12_3' define si la vivienda se ubica en una villa de emergencia. 1=si. 2=no

    st.subheader("CANTIDAD DE VIVIENDAS UBICADAS EN VILLAS EMERGENCIA POR AGLOMERADO")



    mask = 