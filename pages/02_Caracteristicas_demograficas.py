#Pagina de ger 
import streamlit as st
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

from src.utils.parte_2.P3.grafico_de_barras import generar_barras
boton = st.button("Ingresar anio y luego trimestre")
if boton:
    generar_barras()