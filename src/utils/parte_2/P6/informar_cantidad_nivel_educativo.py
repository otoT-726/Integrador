import pandas as pd
import matplotlib.pyplot as grafico
import matplotlib.ticker as ticker
from pathlib import Path
from src.utils.rutas import data_path

detalle = data_path / "archivo_individuos.txt"
index_nivelEd = 'NIVEL_ED'
index_pondera = 'PONDERA'

def informar_cantidad_nivelEd(anio):
    data = pd.read_csv(detalle, sep=';', encoding='utf-8', low_memory=False)
    
    # Filtra por año
    data_filtrada = data[data['ANO4'] == anio]
    
    if data_filtrada.empty:
        return None  # Para que Streamlit maneje este caso y muestre un mensaje

    # Agrupa y suma
    cantidades_niveles = data_filtrada.groupby(index_nivelEd)[index_pondera].sum()
    
    # Crear gráfico
    fig, ax = grafico.subplots(figsize=(10, 6))
    cantidades_niveles.plot(kind='bar', color='red', ax=ax)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'.replace(',', '.')))
    
    grafico.title('Cantidad de personas por nivel educativo')
    grafico.xlabel('Nivel Educativo')
    grafico.ylabel('Cantidad de Personas (ponderadas)')
    grafico.xticks(rotation=0)
    grafico.tight_layout()
    
    return fig
