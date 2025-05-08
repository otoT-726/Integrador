import csv
import streamlit as st
from src.utils.primerUltimoTrimAno import primerUltimoTrimAno
from src.utils.agregar_archivo import agregar_trimestre_completo_hogar, agregar_trimestre_completo_individuo
from src.utils.rutas import data_path

#CONFIGURACIÓN DE LA PÁGINA

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
st.button("Recargar información")

st.divider()
#vamos a crear una lista con los archivos que ya tenemos en la base de datos


def agregar(listaArchivos,data_path):
    for archivo in data_path.iterdir(): # vamos a recorrer los archivos que hay en la carpeta de datos
        #for elem in listaArchivos:
        if archivo.name not in listaArchivos:   #saco el [0]
            listaArchivos.append(archivo.name)
            
            with open(ruta_nombres, "w") as nombres:
                csv.writer(nombres, delimiter=";").writerow(listaArchivos)

            if "hogar" in archivo.name.lower():
                agregar_trimestre_completo_hogar(archivo)
                st.success(f"Se ha agregado el archivo {archivo.name} a la base de datos de hogares")
                #se agrego a la lista de nuestros archivos ya cargados,uno nuevo                    
            elif "indi" in archivo.name.lower() :
                agregar_trimestre_completo_individuo(archivo)
                st.success(f"Se ha agregado el archivo {archivo.name} a la base de datos de individuos")


ruta_nombres = data_path / "ruta_nombres.txt"
with open(ruta_nombres) as file:
    listaArchivos = list(csv.reader(file, delimiter= ";"))[0]
    with st.expander("Archivos en la base de datos"):
        for nombre in listaArchivos:
            st.write(nombre)
    if st.button("Agregar archivos nuevos"):
        agregar(listaArchivos,data_path)
        st.success("Archivos agregados correctamente")

