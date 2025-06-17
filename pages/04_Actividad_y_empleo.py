import streamlit as st
import pandas as pd
from pathlib import Path

from src.utils.parte_2.P5.evolucion_desempleo import data_frame_empleo
from src.utils.rutas import data_path
from src.utils.parte_2.P5.desocupadas_estudios import mostrar_desocupadas_estudios
from src.utils.parte_2.P5.porcentaje_estatal import retornar_informacion_trabajadores


# Página de Actividad y Empleo
mostrar_desocupadas_estudios()

# Ruta al archivo
detalle_individuos = data_path / "archivo_individuos.txt"
index_aglomerados = 'AGLOMERADO'

# Cargamos aglomerados únicos
df_individuos = pd.read_csv(detalle_individuos, sep=";")
aglomerados_disponibles = sorted(df_individuos[index_aglomerados].unique().tolist())
aglomerados_disponibles.insert(0, "Todo el país")  # Opción para todo el país

# Título
st.subheader("Gráfico de evolución del desempleo y empleo por aglomerado / país")
st.write("Seleccione un aglomerado para ver la evolución del desempleo y empleo en el tiempo:")

# Selector
aglomerado_seleccionado = st.selectbox("Seleccione un aglomerado:", aglomerados_disponibles)

# Lógica para convertir a None si es “Todo el país”
aglomerado_param = None if aglomerado_seleccionado == "Todo el país" else aglomerado_seleccionado

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