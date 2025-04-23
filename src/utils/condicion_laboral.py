#5.​ Se debe crear una nueva columna denominada CONDICION_LABORAL de formato
#texto. La transformación debe seguir las siguientes reglas:Trabajo Integrador 2025 - Seminario de Lenguajes Opción Python
#-​Ocupado autónomo: si ESTADO es igual a 1 y CAT_OCUP es 1 o 2.
#-​Ocupado dependiente: si ESTADO es igual a 1 y CAT_OCUP es 3 o 4 o 9.
#-​Desocupado: si ESTADO es igual a 2.
#-​Inactivo: si ESTADO es igual a 3.
#-​Fuera de categoría/sin información: si ESTADO es igual a 4

import csv

def agregar_condicion_laboral(maestro):
    index_estado = 27
    index_cat_ocup = 28
    with open (maestro) as archivo:
        csv_reader = csv.reader(archivo, delimiter=";")
        filas = list(csv_reader)
        filas[0].append("CONDICION_LABORAL")
        for fila in filas[1:]:
            estado = fila[index_estado]
            cat_ocup = fila[index_cat_ocup]
            if estado == "1":
                if cat_ocup == "1" or cat_ocup == "2":
                    fila.append("Ocupado autónomo")
                elif cat_ocup == "3" or cat_ocup == "4" or cat_ocup == "9":
                    fila.append("Ocupado dependiente")
            elif estado == "2":
                fila.append("Desocupado")
            elif estado == "3":
                fila.append("Inactivo")
            else:
                fila.append("Fuera de categoría/sin información")
                
    with open(maestro, "w", newline="") as archivo:
        csv_writer = csv.writer(archivo, delimiter=";")
        csv_writer.writerows(filas)