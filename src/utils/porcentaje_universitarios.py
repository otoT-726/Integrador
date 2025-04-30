import csv
from src.utils import diccionario_aglomerados

def porcentaje_universitarios_aglomerados(ruta):
    """ Informa el porcentaje de personas que hayan cursado al menos en 
        nivel universitario o superior por aglomerado"""
    

    dicci_porcentajes = {clave: 0 for clave in diccionario_aglomerados.keys()}
    dicci_total = {clave: 0 for clave in diccionario_aglomerados.keys()}
    with open(ruta) as archivo:
        csv_dict = csv.DictReader(archivo, delimiter=";")

        #Guardo los datos correspondientes en diccionarios
        for linea in csv_dict:                                                            
            if(linea["CH12"] > "6" and linea["CH12"] < "9"):
                dicci_porcentajes[int(linea["AGLOMERADO"])] += int(linea["PONDERA"])
            dicci_total[int(linea["AGLOMERADO"])] += int(linea["PONDERA"])

    #Transformo las cantidades crudas en porcentajes
    for clave, valor in dicci_porcentajes.items():                                        
        dicci_porcentajes[clave] = (100/dicci_total[clave]) * valor
    mensaje = "Porcentaje de propietarios por región "
    print(f"{mensaje:^55}")
    for clave, valor in dicci_porcentajes.items():
        print(f"Localidad: {diccionario_aglomerados[clave]:<35}: {round(valor, 2)} %")  #-> La funcion round limita los decimales del numero flotante