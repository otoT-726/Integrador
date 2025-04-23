import csv


# Condiciones
# 1 SI ES MAYOR DE EDAD Y COMPLETO LA UNIVERSIDAD
# 2 SI NO ES MAYOR O NO COMPLETO LA UNIVERSIDAD
# 0 ULTIMO CASO SI NO TIENE NINGUNA DE LAS ANTERIORES

index_nivelEd = 26
index_edad = 13

def columna_universitario_numerica(file):
    """Agrega la columna de universitario al archivo de individuos"""
    # Abro el archivo para leer
    with open(file, newline='', encoding='utf-8') as archivo:
        csv_reader = csv.reader(archivo, delimiter=';')
        header = next(csv_reader)  # Me guardo el header en la variable
        header.append('UNIVERSITARIO')  # Agrego nueva columna 'UNIVERSITARIO'
        filas = []  # Aquí guardaré las filas procesadas

        # Recorro el cuerpo del archivo y agrego la nueva columna
        for line in csv_reader:
            if int(line[index_edad]) >= 18 and int(line[index_nivelEd]) == 6:
                line.append(1)  # Si es mayor de edad y completó la universidad
            elif int(line[index_edad]) >= 18 and int(line[index_nivelEd]) != 6:
                line.append(2)  # Si es mayor de edad pero no completó la universidad
            else:
                line.append(0)  # Si no tiene ninguna de las anteriores

            filas.append(line)  # Agrego la fila procesada a 'filas'

    # Escribo el archivo con la nueva columna
    with open(file, 'w', newline='', encoding='utf-8') as archivo:
        csv_writer = csv.writer(archivo, delimiter=';')
        csv_writer.writerow(header)  # Escribo el header
        csv_writer.writerows(filas)  # Escribo las filas procesadas
