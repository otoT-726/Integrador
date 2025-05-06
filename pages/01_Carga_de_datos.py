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

#vamos a crear una lista con los archivos que ya tenemos en la base de datos
listaArchivos = []
for archivos in data_path.iterdir():
    listaArchivos.append(archivos.name)

st.write("Archivos en la base de datos:")
st.write(listaArchivos)

def agregar(listaArchivos,data_path):
    for archivo in data_path.iterdir(): # vamos a recorrer los archivos que hay en la carpeta de datos
        if archivo.name not in listaArchivos:
            if archivo.name.startswith("usu_h"):
                agregar_trimestre(data_path_arch_hogares,archivo)
                st.success(f"Se ha agregado el archivo {archivo.name} a la base de datos de hogares")
                #se agrego a la lista de nuestros archivos ya cargados,uno nuevo
                listaArchivos.append(archivo.name)
            elif archivo.name.startswith("usu_i"):
                agregar_trimestre(data_path_arch_individuos,archivo)
                st.success(f"Se ha agregado el archivo {archivo.name} a la base de datos de individuos")
                listaArchivos.append(archivo.name)

st.button("ACTUALIZAR(MANTENIEMIENTO BY GERMAIN!)", key="agregar_archivo", on_click=agregar, args=(listaArchivos,data_path))