import csv
#EJERCICIO 10 SECCION A
def condicion_de_habitabilidad(ruta) -> None:           #Especifico que la funcion retorna None. Al ejecutarla solo actualiza al archivo
    """
    Recibe el archivo maestro y lo actualiza. Retorna None
    Crea un sistema basandose en la calidad del hogar
    y depende las condiciones cumplidas, la residencia se considera
    insuficiente, regular, saludable o buena.
    """
    with open(ruta) as archivo:
        csv_reader = csv.DictReader(archivo, delimiter=";")
        header, datos = csv_reader.fieldnames + ["CONDICION_DE_HABITABILIDAD"], list(csv_reader)

    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        csv_writer = csv.DictWriter(archivo, fieldnames= header, delimiter=";")
        csv_writer.writeheader
        
        for linea in datos:
            tipo_piso = str(linea["IV3"])
            tiene_agua = str(linea["IV6"])
            tipo_agua = str(linea["IV7"])
            tiene_baño = str(linea["IV8"])
            donde_baño = str(linea["IV9"])
            tipo_baño = str(linea["IV10"])
            if(tiene_agua != "1" or tiene_baño != "1" or tipo_piso == "3" or donde_baño == "3"):        #Si no tiene agua, baño, pisos fijos o baño en su terreno se considera insuficiente
                linea["CONDICION_DE_HABITABILIDAD"] = "Insuficiente"
            elif(tipo_agua == "1" and tipo_baño == "1" and donde_baño == "1" and tipo_piso == "1"):     #Si tiene todas las necesidades basicas cubiertas se considera Buena
                linea["CONDICION_DE_HABITABILIDAD"] = "Buena"
            elif(tipo_agua != "3"  and donde_baño == "1" and tipo_baño != "3"):                         #Si tiene agua y un baño dentro de su casa se considera saludable
                linea["CONDICION_DE_HABITABILIDAD"] = "Saludable"
            else:
                linea["CONDICION_DE_HABITABILIDAD"] = "Regular"                                         #Todas las residencias que no hayan entrado en las variables anteriores,
                                                                                                        # es decir que pueden contar con variedad de condiciones pero no extremas,
                                                                                                        # se las considera regulares
            csv_writer.writerow(linea)
