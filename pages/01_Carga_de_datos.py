import csv
import streamlit as st
import sys

from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))
from src.utils.seccion_b.primer_ultimo_trim_ano import primerUltimoTrimAno

from src.utils.seccion_a.agregar_archivo import agregar_trimestre_completo_hogar, agregar_trimestre_completo_individuo
from src.utils.rutas import data_path
from src.utils.parte_2.verificacion import correspondencias

# CONFIGURACIÓN DE LA PÁGINA

data_path_arch_individuos = data_path / "archivo_individuos.txt"
data_path_arch_hogares = data_path / "archivo_hogares.txt"

st.set_page_config(page_title="Carga de datos", page_icon=":rocket:", layout="wide")

# FRONTEND

st.title('Carga de datos')
st.divider()

try:
    info_fechas_individuos = primerUltimoTrimAno(data_path_arch_individuos)
    info_fechas_hogares = primerUltimoTrimAno(data_path_arch_hogares)

    st.markdown(f"El sistema contiene informacion de individuos desde **el año:  {info_fechas_individuos[0][0]},  trimestre: {info_fechas_individuos[0][1]}**, hasta **el año: {info_fechas_individuos[1][0]}, trimestre: {info_fechas_individuos[1][1]}**")
    st.markdown(f"El sistema contiene informacion de hogares desde **el año:  {info_fechas_hogares[0][0]},  trimestre: {info_fechas_hogares[0][1]}**, hasta **el año: {info_fechas_hogares[1][0]}, trimestre: {info_fechas_hogares[1][1]}**")

except ValueError:
    st.write("El dataset no contiene información de ningun trimestre")

st.write(" ")
st.divider()

ruta_nombres = data_path / "ruta_nombres.txt"

def agregar(data_path, lista_archivos):
    correspondencias_sin_pareja = dict(correspondencias())
    nuevos_archivos = []

    for archivo in data_path.iterdir():
        if archivo.name == "ruta_nombres.txt":
            continue

        if archivo.name not in lista_archivos and archivo.name not in correspondencias_sin_pareja:
            if "usu_hogar" in archivo.name.lower():
                agregar_trimestre_completo_hogar(archivo)
                st.success(f"Se ha agregado el archivo {archivo.name} a la base de datos de hogares")
                nuevos_archivos.append(archivo.name)

            elif "usu_indi" in archivo.name.lower():
                agregar_trimestre_completo_individuo(archivo)
                st.success(f"Se ha agregado el archivo {archivo.name} a la base de datos de individuos")
                nuevos_archivos.append(archivo.name)

        elif archivo.name not in lista_archivos and archivo.name in correspondencias_sin_pareja:
            st.warning(f'El archivo {archivo.name} no tiene correspondencia: {correspondencias_sin_pareja[archivo.name]}.')

    # Actualizar el archivo solo si hubo cambios
    if nuevos_archivos:
        lista_archivos.extend(nuevos_archivos)
        with open(ruta_nombres, "w") as nombres:
            csv.writer(nombres, delimiter=";").writerow(lista_archivos)


with open(ruta_nombres) as file:
    lista_archivos = list(csv.reader(file, delimiter=";"))[0]

    with st.expander("Archivos en la base de datos"):
        for nombre in lista_archivos:
            st.write(nombre)

    if st.button("Agregar archivos nuevos"):
        agregar(data_path, lista_archivos)
        st.success("Archivos agregados correctamente")
