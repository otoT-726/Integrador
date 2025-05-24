import csv
def primerUltimoTrimAno(archivo):
    listaFechas = []
    with open(archivo, encoding = "utf-8") as arch:
        csv_dict_reader = csv.DictReader(arch, delimiter = ";")
        for linea in csv_dict_reader:
            ano = int(linea["ANO4"])
            trim = int(linea["TRIMESTRE"])
            
            anoTrim = (ano, trim)
            listaFechas.append(anoTrim)
        
        min_fecha = min(listaFechas)
        max_fecha = max(listaFechas)
        
    
    return min_fecha, max_fecha
        