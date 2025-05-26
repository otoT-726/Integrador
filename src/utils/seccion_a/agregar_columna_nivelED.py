import csv
from utils.rutas import data_path
#EJERCICIO 4 SECCION A

def addNivelED(archivo_individuos):
        """La funcion agrega la columna del nivel educativo al archivo de detalle de individuos recibido para agregarlo al maestro"""
        index_nivelED = "NIVEL_ED"
        # diccionario donde me guardare dos columnas del detalle para luego invocar para agregar en el maestro
        # traigo el archivo maestro
        with open(archivo_individuos) as mae:
                csv_reader = csv.DictReader(mae, delimiter=";")
                header = csv_reader.fieldnames + ["NIVEL_ED_str"]
                filas = []

                for dat in csv_reader:
                        nivel = dat[index_nivelED]
                        match nivel:
                                case "1": dat["NIVEL_ED_str"] = "Primario incompleto"
                                case "2": dat["NIVEL_ED_str"] = "Primario completo"
                                case "3": dat["NIVEL_ED_str"] = "Secundario incompleto"
                                case "4": dat["NIVEL_ED_str"] = "Secundario completo"
                                case "5": dat["NIVEL_ED_str"] = "Superior"
                                case "6": dat["NIVEL_ED_str"] = "Universitario"
                                case "7" | "9": dat["NIVEL_ED_str"] = "Sin informacion"

        # luego agrego el nivel educativo tambien a la fila,pero quedara modificada la fila con el nuevo dato agregado
                filas.append(dat)

        with open(archivo_individuos, "w", newline='') as mae:
                # writter para indicar que voy a escribir el archivo
                csv_writer = csv.DictWriter(mae, delimiter=";", fieldnames=header)
                csv_writer.writeheader()
                # con el writerow voy a escribir la linea dat
                csv_writer.writerows(filas)
