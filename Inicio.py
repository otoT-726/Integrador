import streamlit as st

#Un título con el nombre de la aplicación (el que ustedes deseen).
#Un pequeño párrafo explicando brevemente la información que se almacena, es
#decir, que contiene la EPH.
#En la etapa 2 se agrega las indicaciones de uso de la interfaz.

#CONFIGURACIÓN DE LA PÁGINA

st.set_page_config(page_title="Encuest App", page_icon=":rocket:", layout="wide")#CONFIGURACION DEL TITULO EN PESTAÑA Y EL ICONO

# FRONTEND

st.title("Encuest App")

st.divider()

st.subheader("¿Qué es la Encuesta Permanente de Hogares?")

st.write("La Encuesta Permanente de Hogares (EPH) es un programa nacional de producción permanente de indicadores sociales" \
" cuyo objetivo es conocer las características socioeconómicas de la población." \
" Es realizada en forma conjunta por el Instituto Nacional de Estadística y Censos (INDEC) y las Direcciones Provinciales de Estadística (DPE)")
