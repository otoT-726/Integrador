import csv
#EJERCICIO 3 SECCION A
def addColumna(archivo_individuos):
    """Agrega la columna de genero al archivo de detalle de individuos recibido para agregarlo al maestro"""
    index_genero = "CH04"
    #traigo el archivo maestro
    with open(archivo_individuos, "r",newline='') as mae:
        csv_reader = csv.DictReader(mae, delimiter=";")
        header = csv_reader.fieldnames + ["CH04str"]
        filas = []

        for dat in csv_reader:
            if dat[index_genero] == "1":
                dat["CH04str"] = "Masculino"
            else :
                dat["CH04str"] = "Femenino"
            
            filas.append(dat) # dat es la linea,que es una lista, entonces a esa linea le agrego el genero y quedara modificada

    with open(archivo_individuos, "w",newline='') as mae:
        csv_writer = csv.DictWriter(mae,delimiter=";", fieldnames=header) # writter para indicar que voy a escribir el archivo
        csv_writer.writeheader()
        csv_writer.writerows(filas) # con el writerow voy a escribir la linea dat