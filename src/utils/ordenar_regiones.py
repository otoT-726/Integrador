import csv

def ordenar_regiones(archivo_hogares):
    with open(archivo_hogares, "r") as archivo:
        csv_dict_reader = csv.DictReader(archivo, delimiter=";")
        dict_inquilinos_por_region = {}
        dict_por_region_total = {}
        for fila in csv_dict_reader:       
            region = fila["REGION"]
            pondera = int(fila["PONDERA"])
            inquilino_o_no = int(fila["II7"])
            if region not in dict_por_region_total:
                dict_por_region_total[region] = pondera
            else:
                dict_por_region_total[region] += pondera
                
            if(inquilino_o_no == 3):
                if region not in dict_inquilinos_por_region:
                    dict_inquilinos_por_region[region] = pondera
                else:
                    dict_inquilinos_por_region[region] += pondera
        # Creo el diccionario de porcentajes de inquilinos por region.
        dict_porcentaje_inquilinos = {}
        for region, total in dict_por_region_total.items():
            dict_porcentaje_inquilinos[region] = (dict_inquilinos_por_region[region] / total) * 100 
                      
        # Ordeno el diccionario por la cantidad de personas
        dict_regiones_ordenado = dict(sorted(dict_porcentaje_inquilinos.items(), key=lambda item: item[1], reverse=True))
        
        #retornar el diccionario ordenado
        return dict_regiones_ordenado