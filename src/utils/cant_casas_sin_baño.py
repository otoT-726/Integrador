import csv
from src.utils import diccionario_aglomerados

def aglomerado_con_menos_baños(ruta) -> None:
    """ Devuelve el aglomerado con mayor cantidad de casas con más de dos habitantes que no cuenten con baño"""


    dicci_sin_baños = {clave: 0 for clave in diccionario_aglomerados.keys()}

    with open(ruta) as archivo:
        csv_dict = csv.DictReader(archivo, delimiter=";")

        for linea in csv_dict:
            if(linea["II9"] == "4" and linea["IX_TOT"] > "2"):
                dicci_sin_baños[int(linea["AGLOMERADO"])] += int(linea["PONDERA"])
    maxaglomerado = max(dicci_sin_baños.items(), key=lambda x: x[1])
    print(f'La región con más casas con mas de dos habitantes y sin baño es {diccionario_aglomerados[maxaglomerado[0]]}, con {maxaglomerado[1]} viviendas en estas condiciones.')
