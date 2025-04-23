import csv
def addColumna(archivo_individuos):
    index_genero = 11
    #traigo el archivo maestro
    with open(archivo_individuos, "r",newline='') as mae:
        csv_reader = csv.reader(mae, delimiter=";")
        header, cuerpo = next(csv_reader) ,list(csv_reader) 

    with open(archivo_individuos, "w",newline='') as mae:
        csv_writer = csv.writer(mae,delimiter=";") # writter para indicar que voy a escribir el archivo
        header.append("CH04str")                                        
        csv_writer.writerow(header)     # es para escribir una linea, en este caso para el header                          
        for dat in cuerpo:
            if dat[index_genero] == "1":
                genero_str = "Masculino"
            else :
                genero_str = "Femenino"
            dat.append(genero_str) # dat es la linea,que es una lista, entonces a esa linea le agrego el genero y quedara modificada
            csv_writer.writerow(dat) # con el writerow voy a escribir la linea dat 