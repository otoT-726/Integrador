#Pagina de ger 
import streamlit as st
import sys
import pandas as pd
from pathlib import Path
from src.utils.rutas import data_path
import numpy as np
import matplotlib.pyplot as plt
import altair as alt        

sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

from src.utils.parte_2.P3.grafico_de_barras import generar_barras
from src.utils.seccion_b.primer_ultimo_trim_ano import primerUltimoTrimAno
min_fecha, max_fecha = primerUltimoTrimAno(data_path / "archivo_individuos.txt")
index_anio = "ANO4"
index_trimestre = "TRIMESTRE"
index_aglomerado = "AGLOMERADO"
index_edad = "CH06"
index_pondera = "PONDERA"
datos = pd.read_csv(data_path / "archivo_individuos.txt", sep=";",low_memory=False)

años = (datos[index_anio].unique())
trim = (datos[index_trimestre].unique())
años_trimestres = (tuple([(int(año), int(trimestre)) for año in años for trimestre in trim]))
# en esta pagina se muestran la informacion y en otra tabla muestro los graficos


tab1, tab2 = st.tabs(["Información", "Visualización"])
with tab1:
    st.title("Caracteristicas demograficas de la poblacion")
    st.subheader("En esta sección se visualizará información relacionada a las características demográficas de la población argentina según la EPH.")
    st.divider() 
    st.write("1.1")   
    st.write("En esta sección se generará un gráfico de barras que muestre la distribución de la población por grupos de edad (cada 10 años) y sexo. El gráfico tendrá barras dobles (una para cada sexo) por cada grupo de edad. Para ello se solicitará al usuario que ingrese un año y trimestre, y se validará que el año se encuentre entre los cuales se tiene información.")
    st.write(f'Los años y trimestres que se encuentran disponibles son desde el año : {min_fecha[0]}, trimestre : {min_fecha[1]}, hasta año : {max_fecha[0]}, trimestre {max_fecha[1]}.')
    boton = st.chat_input("Ingrese año y trimestre ej : 2023, 3, el grafico se generar en el apartado de visualizacion")
    if boton:
        st.write("Se ingreso el año y trimestre: ", boton)
    else:
        st.write("Ingrese un año y trimestre para generar el gráfico de barras.")
    st.divider()
    st.write("1.2")
    ult_anio = max_fecha[0]
    ult_trim = max_fecha[1]


    st.write(f"En esta seccion se mostrara una tabla que muestra la edad promedio de personas para el ultimo trimestre {ult_trim} y año {ult_anio} del cual se tenga informacion, agrupado por aglomerado. El aglomerado es una variable que indica la zona geográfica de residencia de la persona.")

    # Me traigo los datos del dataset del ultimo trimestre y año
    #data filtrada es un dataframe ahora que solo tiene los datos del ultimo trimestre y año de todo el dataset
    #                               estos son columnas booleanas 
    dataFiltrada = datos[datos[index_anio] == ult_anio][datos[index_trimestre] == ult_trim]

    #necesito agrupar por aglomerado y calcular la edad promedio
    #para eso tambien necesito que la edad, entonces tomo de dataFiltrada el index_edad y luego me voy agrupando por el index aglomerado
    promedio = datos[index_edad].groupby(dataFiltrada[index_aglomerado]).mean()
    # las agrupo por el aglomerado y calculo la media
    # que el numero que se muestre como promedio sea un numero con 0 decimales
    promedio = promedio.round(0).astype(int)
    st.write(promedio)
    
    st.divider()
    st.write("1.3")
    st.write("En esta seccion se generará un gráfico que muestre la evolución de la dependencia demográfica para todos los años y trimestres del dataset.")
    st.write("Seleccione un aglomerado para mostrar la evolucion de la dependencia demografica para todos los años y trimestres del dataset")
    # traigo del dataset los aglomerados unicos!
    opciones = datos[index_aglomerado].unique()
    # los ordeno para que aparezcan ordenados
    opciones = sorted(opciones)

    opcion = st.selectbox("Opciones a elegir",opciones,index=None,placeholder="Seleccione un aglomerado, el grafico se mostrara en la pestaña de visualizacion")
    # La dependencia demográfica se define como el cociente de la cantidad de población de 0 a 
    # 14 años y mayores de 65 (se asumen jubilados) respecto a la población en edad activa 
    # (15 a 64 años) multiplicado por 100.
    st.divider()
    st.write("1.4")
    st.write("En esta seccion se informara para cada año y trimestre almacenado la media  y mediana edad de la poblacion")

    filtro = datos.groupby([index_anio, index_trimestre])[index_edad].agg(['mean', 'median']).reset_index()
    filtro = filtro.rename(columns={'ANO4': 'Año', 'TRIMESTRE': 'Trimestre','mean': 'Edad Media', 'median': 'Edad Mediana'})
    st.write(filtro)

with tab2:
    st.subheader("1.1")
    st.subheader("Grafico de barras de la poblacion por grupos de edad y sexo del año y trimestre ingresado")
    if boton:
        try:
            info_masculino, info_femenina = generar_barras(boton,años_trimestres)
            #crear grafico de barras 
            grupos = ["10","20","30","40","50","60","70","80","90","100"]
            x = np.arange(len(grupos))  # la ubicacion de las barras

            fig1, ax1 = plt.subplots(figsize=(8, 5))
            ax1.bar(x, info_masculino, color='skyblue')
            ax1.set_title("Distribución por edad - Masculino")
            ax1.set_xlabel("Grupo de edad (años)")
            ax1.set_ylabel("Población ponderada")
            ax1.set_xticks(x)
            ax1.set_xticklabels(grupos)

            # Gráfico femenino
            fig2, ax2 = plt.subplots(figsize=(8, 5))
            ax2.bar(x, info_femenina, color='lightpink')
            ax2.set_title("Distribución por edad - Femenino")
            ax2.set_xlabel("Grupo de edad (años)")
            ax2.set_ylabel("Población ponderada")
            ax2.set_xticks(x)
            ax2.set_xticklabels(grupos)

            # Mostrar gráficos uno al lado del otro
            col1, col2 = st.columns(2)
            with col1:
                st.pyplot(fig1)
            with col2:
                st.pyplot(fig2)

        except Exception as e:
            st.error("Hubo un error procesando los datos. Verifique que el formato sea correcto (ej. 2022, 3).")
            st.exception(e)
    st.divider()
    st.subheader("1.3")
    # voy a tomar todos los datos del dataset DEL AGLOMERADO ELEGIDO
    if opcion:
        dataFiltrada_x_aglomerado = datos[datos[index_aglomerado]== opcion]
        # necesito agrupar por año y el trimestre y edad        columnas                                         quedan las columnas
        grupo = dataFiltrada_x_aglomerado.groupby([index_anio, index_trimestre,index_edad])[index_pondera].sum().reset_index()
        # separo los grupos de edades
        grupo_edad_14 = grupo[grupo[index_edad] <= 14]
        grupo_edad_65 = grupo[grupo[index_edad] >= 65]
        grupo_edad_15_64 = grupo[grupo[index_edad] > 14][grupo[index_edad] < 65]

        #en estas 3 lineas agrupo por los años y trimestres y acumulo la ponderacion
        grupo_edad_14 = grupo_edad_14.groupby([index_anio, index_trimestre])[index_pondera].sum().reset_index()
        grupo_edad_65 = grupo_edad_65.groupby([index_anio, index_trimestre])[index_pondera].sum().reset_index()
        grupo_edad_15_64 = grupo_edad_15_64.groupby([index_anio, index_trimestre])[index_pondera].sum().reset_index()

        # aca junto los 3 grupos de edad en un solo dataframe
        grupo_completo = grupo_edad_14.merge(grupo_edad_65, on=[index_anio, index_trimestre])
        grupo_completo = grupo_completo.merge(grupo_edad_15_64, on=[index_anio, index_trimestre])

        # renombro las columnas para que sea mas facil de entender
        grupo_completo = grupo_completo.rename(columns={'PONDERA_x': 'poblacion_joven','PONDERA_y': 'poblacion_mayor','PONDERA': 'poblacion_activa'})

        # creo una nueva columna que calcule la dependencia demografica
        grupo_completo['dependencia_demografica'] = ((grupo_completo['poblacion_joven'] + grupo_completo['poblacion_mayor']) / grupo_completo['poblacion_activa']) * 100

        grupo_completo['Periodo'] = grupo_completo[index_anio].astype(str) + 'T' + grupo_completo[index_trimestre].astype(str)

        # Crear gráfico con Altair
        chart = alt.Chart(grupo_completo).mark_line(point=True).encode(
            x=alt.X('Periodo:N', title='Periodo'),
            y=alt.Y('dependencia_demografica:Q',scale=alt.Scale(domain=[grupo_completo['dependencia_demografica'].min() - 0.05,grupo_completo['dependencia_demografica'].max() + 0.05]),
                title='Dependencia Demográfica (%)'),
        tooltip=['Periodo', 'dependencia_demografica']).properties(width=600,height=400,title='Evolución de la Dependencia Demográfica para el aglomerado: ' + str(opcion))

        # Mostrar gráfico en Streamlit
        st.altair_chart(chart, use_container_width=True)



