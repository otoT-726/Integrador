import csv
#EJERCICIO 7 SECCION A
index_miembros = "IX_TOT" #64


def columna_tipo_de_casa(file): 
    """Agrega la columna de tipo de casa al archivo de hogares"""
    with open(file, newline='') as archivo:
        csv_reader = csv.DictReader(archivo, delimiter=';')
        header = csv_reader.fieldnames + ['TIPO_HOGAR']  # Agrego nueva columna 'TIPO_HOGAR'
        filas = []  # Me guardo las filas procesadas
        
        for line in csv_reader:
            if line[index_miembros] == "1":
                line["TIPO_HOGAR"] = 'Unipersonal'
            elif line[index_miembros] >= "2" and line[index_miembros] <= "4":
                line["TIPO_HOGAR"] = 'Nuclear'
            else:
                line["TIPO_HOGAR"] = 'Extendido'
            filas.append(line)

    #Agrego la nueva columna al archivo
    with open(file, 'w', newline='',encoding='utf-8') as archivo:
        csv_writer = csv.DictWriter(archivo, fieldnames=header, delimiter=';')
        csv_writer.writeheader()  # Escribo el header
        csv_writer.writerows(filas)  # Escribo las filas