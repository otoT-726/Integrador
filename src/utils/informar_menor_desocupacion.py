import csv 

def informe_menor_desocupacion(archivo_hogares):
    """
        Genera un informe de la cantidad de personas desocupadas por hogar.
        el resultado se imprime en pantalla 
    """
    with open(archivo_hogares, "r") as archivo:
        cant_desocupados = 0
        ano_actual = ""
        trim_actual = ""
        ano_minimo = ""
        trim_minimo = ""
        minimo_desocupados = 9999
        
        csv_dict_reader = csv.DictReader(archivo, delimiter=";")
        for fila in csv_dict_reader:
            ano = fila["ANO4"]
            trim = fila["TRIMESTRE"]
            pondera = int(fila["PONDERA"])

            if fila["CONDICION_LABORAL"] == "Desocupado":
                cant_desocupados += pondera
            
            if ano != ano_actual or trim != trim_actual:
                if cant_desocupados < minimo_desocupados:
                    minimo_desocupados = cant_desocupados
                    ano_minimo = ano
                    trim_minimo = trim

                ano_actual = ano
                trim_actual = trim
                cant_desocupados = pondera if fila["CONDICION_LABORAL"] == "Desocupado" else 0
        # Verificar el último hogar
        if cant_desocupados < minimo_desocupados:
            minimo_desocupados = cant_desocupados
            ano_minimo = ano
            trim_minimo = trim
    print(f"El hogar con menor cantidad de desocupados es el año {ano_minimo} y trimestre {trim_minimo} con {minimo_desocupados} desocupados.")
                