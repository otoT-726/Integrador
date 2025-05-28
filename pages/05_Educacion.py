import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from src.utils.parte_2.P6.informar_cantidad_nivel_educativo import informar_cantidad_nivelEd 

#Archivo individuos


anio = st.number_input("Ingrese el año para el cual desea ver la cantidad de personas por nivel educativo:", min_value=2023, max_value=2024)

if st.button("Grafico personas por nivel educativo"):
    fig = informar_cantidad_nivelEd(anio)
    if fig:
        st.pyplot(fig)
    else:
        st.warning(f"No hay datos disponibles para el año {anio}.")
