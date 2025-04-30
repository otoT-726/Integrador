import csv

def condicion_de_habitabilidad(ruta) -> None:           #Especifico que la funcion retorna None. Al ejecutarla solo actualiza al archivo
    """
    Recibe el archivo maestro y lo actualiza. Retorna None
    Crea un sistema de puntajes basandose en la calidad del hogar
    y depende el puntaje obtenido, la residencia se considera
    insuficiente, regular, saludable o buena.
    """
    with open(ruta) as archivo:
        csv_reader = csv.reader(archivo, delimiter=";")
        header, datos = next(csv_reader), list(csv_reader)

    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        csv_writer = csv.writer(archivo, delimiter=";")
        header.append("CONDICION_DE_HABITABILIDAD")
        csv_writer.writerow(header)
        for linea in datos:
            tipo_piso = str(linea[12])
            tiene_agua = str(linea[16])
            tipo_agua = str(linea[17])
            tiene_baño = str(linea[19])
            donde_baño = str(linea[20])
            tipo_baño = str(linea[21])
            if(tiene_agua != "1" or tiene_baño != "1" or tipo_piso == "3" or donde_baño == "3"):
                linea.append("Insuficiente")
            elif(tipo_agua == "1" and tipo_baño == "1" and donde_baño == "1" and tipo_piso == "1"):
                linea.append("Buena")
            elif(tipo_agua != "3"  and donde_baño == "1" and tipo_baño != "3"): 
                linea.append("Saludable")
            else:
                linea.append("Regular")
            csv_writer.writerow(linea)
