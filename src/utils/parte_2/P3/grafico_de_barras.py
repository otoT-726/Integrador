'''Generar un gráfico de barras que muestre la distribución de la población por grupos de 
edad (cada 10 años) y sexo. El gráfico debe tener barras dobles (una para cada sexo) por 
cada grupo de edad. Para ello se debe solicitar al usuario que ingrese un año y trimestre. 
También se debe validar que el año se encuentre entre los cuales se tiene información.'''
#1

from src.utils.rutas import data_path
from src.utils.seccion_b.primer_ultimo_trim_ano import primerUltimoTrimAno
min_fecha, max_fecha = primerUltimoTrimAno(data_path / "archivo_individuos.txt")


import streamlit as st
import pandas as pd
import sys
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

def obtener_grupo_edad(edad):
    #¿QUE EDAD TIENE?
    if pd.isnull(edad):
        return "Desconocido"
    elif edad >= 0 and edad < 10:
        return "10"
    elif edad < 20:
        return "20"
    elif edad < 30:
        return "30"
    elif edad < 40:
        return "40"
    elif edad < 50:
        return "50"
    elif edad < 60:
        return "60"
    elif edad < 70:
        return "70"
    elif edad < 80:
        return "80"
    elif edad < 90:
        return "90"
    elif edad < 100:
        return "100"
    else:
        return "100+"


index_trimestre = "TRIMESTRE"
index_anio = "ANO4"
index_genero = "CH04str"
index_edad = "CH06"
index_pondera = "PONDERA"


archivo_individuos = data_path / "archivo_individuos.txt"   
def generar_barras(info,años_trimestres, archivo=archivo_individuos):

    diccionarioDecadasMasc = {}
    diccionarioDecadasFem = {}

    #validar informacion ingresada por el usuario
    info = info.split(",")  # Separar el año y trimestre por coma
    anio = int(info[0])
    trimestre =int(info[1])

    if (anio, trimestre) in años_trimestres:
        # Filtrar los datos por año y trimestre 
        data = pd.read_csv(archivo, sep=";")
        # Son mis dos estructuras de datos donde esta la informacion filtrada por anio y trimestre
        data_masculina = (data[(data[index_anio] == anio) & (data[index_trimestre] == trimestre) & (data[index_genero] == 'Masculino')])
        data_femenina = (data[(data[index_anio] == anio) & (data[index_trimestre] == trimestre) & (data[index_genero] == 'Femenino')])  

# Aca se aplica la funcion obtener_grupo_edad a cada edad obtenida del dataframe y se la guarda en una nueva columna llamada 'grupo_edad'
        data_masculina['grupo_edad'] = data_masculina[index_edad].apply(obtener_grupo_edad)
        data_femenina['grupo_edad'] = data_femenina[index_edad].apply(obtener_grupo_edad)   

        # SE CREA EL DICCIONARIO CON LOS GRUPOS DE EDAD Y LA SUMA DE LA PONDERACION POR CADA GRUPO
        diccionarioDecadasMasc = data_masculina.groupby('grupo_edad')[index_pondera].sum().to_dict()
        diccionarioDecadasFem = data_femenina.groupby('grupo_edad')[index_pondera].sum().to_dict()

        # LA LISTA CONTIENE LOS GRUPOS DE EDAD QUE SE VAN A MOSTRAR EN EL GRAFICO
        listaGrupos = ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100"]
# SE ASEGURA QUE CADA GRUPO DE EDAD TENGA UN VALOR, SI NO EXISTE SE ASIGNA 0, Esto es para que si no hay datos de un grupo de edad, se muestre como 0 en el grafico
        contar_masculino = [diccionarioDecadasMasc.get(grupo, 0) for grupo in listaGrupos]  
        contar_femenino = [diccionarioDecadasFem.get(grupo, 0) for grupo in listaGrupos]
    return contar_masculino, contar_femenino