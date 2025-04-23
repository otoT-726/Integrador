import csv

index_miembros = 64


def columna_tipo_de_casa(file): 
    """Agrega la columna de tipo de casa al archivo de hogares"""
    with open(file, newline='', encoding='utf-8') as archivo:
        csv_reader = csv.reader(archivo, delimiter=';')
        header = next(csv_reader)  # Me guardo el header en la variable
        header.append('TIPO_HOGAR')  # Agrego nueva columna 'TIPO_HOGAR'
        filas = []  # Me guardo las filas procesadas
        
        for line in csv_reader:
            if int(line[index_miembros]) == 1:
                line.append('Unipersonal')
            elif int(line[index_miembros]) >= 2 and int(line[index_miembros]) <= 4:
                line.append('Nuclear')
            else:
                line.append('Extendido')
            filas.append(line)

    #Agrego la nueva columna al archivo
    with open(file, 'w', newline='', encoding='utf-8') as archivo:
        csv_writer = csv.writer(archivo, delimiter=';')
        csv_writer.writerow(header)  # Escribo el header
        csv_writer.writerows(filas)  # Escribo las filas