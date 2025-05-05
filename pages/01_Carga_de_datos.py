import streamlit as st
from src.utils.primerUltimoTrimAno import primerUltimoTrimAno
from src.utils.agregar_archivo import agregar_trimestre
from src.utils.rutas import data_path

#CONFIGURACIÓN DE LA PÁGINA

data_path_arch_individuos = data_path / "archivo_individuos.txt"
data_path_arch_hogares = data_path / "archivo_hogares.txt"

st.set_page_config(page_title="Carga de datos", page_icon=":rocket:", layout="wide")

# FRONTEND

st.title('Carga de datos')

st.divider()

info_fechas_individuos = primerUltimoTrimAno(data_path_arch_individuos)
info_fechas_hogares = primerUltimoTrimAno(data_path_arch_hogares)



st.markdown(f"El sistema contiene informacion de individuos desde **el año:  {info_fechas_individuos[0][0]},  trimestre: {info_fechas_individuos[0][1]}**, hasta **el año: {info_fechas_individuos[1][0]}, trimestre: {info_fechas_individuos[1][1]}**")
st.divider()
st.markdown(f"El sistema contiene informacion de hogares desde **el año:  {info_fechas_hogares[0][0]},  trimestre: {info_fechas_hogares[0][1]}**, hasta **el año: {info_fechas_hogares[1][0]}, trimestre: {info_fechas_hogares[1][1]}**")
st.divider()