import streamlit as st
import pandas as pd
from pathlib import Path

from src.utils.parte_2.P5.evolucion_desempleo import data_frame_empleo
from src.utils.rutas import data_path
from src.utils.parte_2.P5.desocupadas_estudios import mostrar_desocupadas_estudios
from src.utils.parte_2.P5.porcentaje_estatal import retornar_informacion_trabajadores

from src.utils import diccionario_aglomerados 

# Página de Actividad y Empleo
mostrar_desocupadas_estudios()

# Ruta al archivo
detalle_individuos = data_path / "archivo_individuos.txt"
index_aglomerados = 'AGLOMERADO'

df_individuos = pd.read_csv(detalle_individuos, sep=";")

# Filtramos los codigos de aglomerados que no son válidos que no están en el diccionario
codigos_aglomerados = sorted(df_individuos[index_aglomerados].unique().tolist())
codigos_aglomerados = [c for c in codigos_aglomerados if c in diccionario_aglomerados.keys()]

# Agregamos el nombre del aglomerado al dataframe
aglomerados_opciones = [(diccionario_aglomerados[c], c) for c in codigos_aglomerados]
aglomerados_opciones.insert(0, ("Todo el país", None))

# Título
st.subheader("Gráfico de evolución del desempleo y empleo por aglomerado / país")
st.write("Seleccione un aglomerado para ver la evolución del desempleo y empleo en el tiempo:")

# Selector
nombre_aglomerado_seleccionado = st.selectbox("Seleccione un aglomerado:", options=[nombre for nombre, _ in aglomerados_opciones]
)

# Obtener el código correspondiente (o None)
aglomerado_param = dict(aglomerados_opciones)[nombre_aglomerado_seleccionado]

# Obtener datos
data_f = data_frame_empleo(aglomerado_param)

# Mostrar gráfico
st.area_chart(
    data_f.set_index("PERIODO")[["tasa_empleo", "tasa_desempleo"]],
    use_container_width=True,
)

st.divider()

# Punto 1.5.4: Informar para cada aglomerado el total de personas ocupadas, el porcentaje con
# empleo estatal, el porcentaje con empleo privado y el porcentaje de otro tipo. Considerar la
# ocupación principal.

st.subheader("TIPOS DE TRABAJO")

st.write("A continuacion se pueden visualizar los datos sobre el tipo de trabajo" \
    " de los individuos en los distintos aglomerados abarcados por la EPH.")

# Retorna un dataframe con el nombre del aglomerado, cantidad de personas con ocupacion, porcentaje
# de trabajadores estatales, privados y de otros tipos. (Ordenados por cantidad de personas ocupadas)
st.write(retornar_informacion_trabajadores(df_individuos))