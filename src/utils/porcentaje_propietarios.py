import csv
from src.utils import diccionario_aglomerados

def porcentaje_propietarios_aglomerado(camino):
    """ Retorna el porcentaje de gente que es propietaria de su domicilio por aglomerado """


    dicci_prop = {clave: 0 for clave in diccionario_aglomerados}  #Hago un diccionario para guardar la cantidad de propietarios por aglomerado

    dicci_total = {clave: 0 for clave in diccionario_aglomerados} #Hago un diccionario para guardar la cantidad total de hogares por aglomerado
    try:
        with open(camino, newline="") as archivo:
            csv_reader = csv.DictReader(archivo, delimiter=";")

            for line in csv_reader:                                           #Guardo el total de hogares por aglomerado, y la cantidad de propietarios
                aglomerado = int(line["AGLOMERADO"])
                dicci_total[aglomerado] += int(line["PONDERA"])
                if(line["II7"] < "3"):
                    dicci_prop[aglomerado] += int(line["PONDERA"])
    except FileNotFoundError:
        print("Error al cargar el archivo. Compruebe la ruta de acceso.")
    #Porcentaje = (100 / total) * cant

    for clave, valor in diccionario_aglomerados.items():                       #Transformo el diccionario de cant_propietarios en un diccionario de porcentaje de propietarios por aglomerado
        try:
            dicci_prop[clave] = (100 / dicci_total[clave]) * dicci_prop[clave]      
        except ZeroDivisionError:
            print(f'Error cargando los datos de {valor}')
    mensaje = "Porcentaje de propietarios por región"
    print(f"{mensaje:^55}")

    for clave, valor in dicci_prop.items():
        print(f"Localidad: {diccionario_aglomerados[clave]:<35}: {round(valor, 2)} %") #-> La funcion round limita los decimales del numero flotante