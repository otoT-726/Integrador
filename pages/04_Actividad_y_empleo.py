import streamlit as st
import pandas as pd
from pathlib import Path


from src.utils.parte_2.P5.evolucion_desempleo import data_frame_empleo
from src.utils.rutas import data_path
from src.utils.parte_2.P5.desocupadas_estudios import mostrar_desocupadas_estudios
from src.utils.parte_2.P5.porcentaje_estatal import retornar_informacion_trabajadores
from src.utils.parte_2.P5.tasas_ocu_desocu import calcular_tasas_por_aglomerado
from src.utils.seccion_b.primer_ultimo_trim_ano import primerUltimoTrimAno
from src.utils.parte_2.P5.traer_coordenadas import extraer_coordenadas

from src.utils import diccionario_aglomerados 

# Página de Actividad y Empleo
mostrar_desocupadas_estudios()

# Ruta al archivo
detalle_individuos = data_path / "archivo_individuos.txt"
index_aglomerados = 'AGLOMERADO'
# Definimos los años y trimestres máximos y mínimos
min_fecha = primerUltimoTrimAno(detalle_individuos)[0]
aniomin, trimmin = min_fecha[0], min_fecha[1]
max_fecha = primerUltimoTrimAno(detalle_individuos)[1]
aniomax, trimmax = max_fecha[0], max_fecha[1]


df_individuos = pd.read_csv(detalle_individuos, sep=";")

tasas_iniciales = calcular_tasas_por_aglomerado(df_individuos, aniomax, trimmax)
tasas_finales = calcular_tasas_por_aglomerado(df_individuos, aniomin, trimmin)

aglomerados_disponibles = sorted(df_individuos[index_aglomerados].unique().tolist())
aglomerados_disponibles.insert(0, "Todo el país")  # Opción para todo el país
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

st.divider()
st.write("A continuacion se pueden visualizar las tasas de empleo y desempleo por aglomerado")
# Mostrar tasas de empleo y desempleo por aglomerado
st.subheader("Tasas de empleo y desempleo por aglomerado")

df_inicio = pd.DataFrame(tasas_iniciales)
df_final = pd.DataFrame(tasas_finales)

# elegir entre tasas de empleo o desempleo para ver
tipo_tasa = st.selectbox(
    "Seleccione el tipo de tasa a visualizar:",
    ["Tasa de Empleo", "Tasa de Desempleo"]
)  

#me traigo el diccionario de coordenadas
dic_coordenadas = extraer_coordenadas()

lista_coordenadas = []
# Agregar coordenadas al DataFrame de tasas iniciales y finales
for cod, datos in dic_coordenadas.items():
    lista_coordenadas.append({
        "AGLOMERADO":int(cod),
        "Nombre": datos["nombre"],
        "Latitud": datos["coordenadas"][0],
        "Longitud": datos["coordenadas"][1]
    })




df_coordenadas = pd.DataFrame(lista_coordenadas)
df_mapa = df_final.merge(df_inicio, on="AGLOMERADO")
df_mapa = df_mapa.merge(df_coordenadas, on="AGLOMERADO")
# mostrar mapa Al elegir la tasa de empleo se deben ver puntos verdes en los aglomerados cuya tasa
#de empleo aumentó con el correr del tiempo. Rojo en el caso contrario.
#Al elegir la tasa de desempleo se deben ver puntos rojos en los aglomerados cuya
#tasa de desempleo aumentó con el correr del tiempo. Verde en el caso contrario.
st.subheader("Mapa de tasas de empleo y desempleo por aglomerado")
st.write("A continuacion se puede visualizar un mapa con las tasas de empleo y desempleo por aglomerado. " \
         "Los puntos verdes indican un aumento en la tasa de empleo, mientras que los puntos rojos indican un aumento en la tasa de desempleo.")        

# Crear un mapa centrado en Argentina
mapa = folium.Map(location=[-38.4161, -63.6167], zoom_start=4)
#mostrar mapa

for index, row in df_mapa.iterrows():
    if tipo_tasa == "Tasa de Empleo":
        color = "green" if row["Tasa Empleo_y"] > row["Tasa Empleo_x"] else "red"
    else:
        color = "red" if row["Tasa Desempleo_y"] > row["Tasa Desempleo_x"] else "green"

    folium.CircleMarker(
        location=[row["Latitud"], row["Longitud"]],
        radius=10,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.6,
    ).add_to(mapa)
    
st_folium(mapa, width=700, height=500)