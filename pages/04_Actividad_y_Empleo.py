from src.utils.parte_2.P5.desocupadas_estudios import mostrar_desocupadas_estudios

mostrar_desocupadas_estudios()

import streamlit as st
import pandas as pd
from pathlib import Path
from src.utils.parte_2.P5.evolucion_desempleo import data_frame_empleo
from src.utils.rutas import data_path

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