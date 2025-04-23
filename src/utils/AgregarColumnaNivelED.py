import csv
def addNivelED(archivo_individuos):
    index_nivelED = 26
    # diccionario donde me guardare dos columnas del detalle para luego invocar para agregar en el maestro                              
    #traigo el archivo maestro
    with open(archivo_individuos, "r") as mae:
        csv_reader = csv.reader(mae, delimiter=";")
        header, cuerpo = next(csv_reader), list(csv_reader)

    with open(archivo_individuos, "w",newline='') as mae:
        csv_writer = csv.writer(mae, delimiter=";") # writter para indicar que voy a escribir el archivo                                  
        header.append("NIVEL_ED_str") 
        csv_writer.writerow(header)     # es para escribir una linea, en este caso para el header                         
        for dat in cuerpo:
            nivel = dat[index_nivelED]
            match nivel :
                case "1":
                        nivel_str = "Primario incompleto"
                case "2":
                        nivel_str = "Primario completo"
                case "3":
                        nivel_str = "Secundario incompleto"
                case "4":
                        nivel_str = "Secundario completo"
                case "5":
                        nivel_str = "Superior"
                case "6":
                        nivel_str = "Universitario"
                case "7" | "9" :
                        nivel_str = "Sin informacion"
            dat.append(nivel_str) # luego agrego el nivel educativo tambien a la fila,pero quedara modificada la fila con el nuevo dato agregado
            csv_writer.writerow(dat) # con el writerow voy a escribir la linea dat 