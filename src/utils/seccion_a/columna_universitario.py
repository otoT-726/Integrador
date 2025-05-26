import csv
# EJERCICIO 6 SECCION A

# Condiciones
# 1 SI ES MAYOR DE EDAD Y COMPLETO LA UNIVERSIDAD
# 2 SI NO ES MAYOR O NO COMPLETO LA UNIVERSIDAD
# 0 ULTIMO CASO SI NO TIENE NINGUNA DE LAS ANTERIORES

index_nivelEd = "NIVEL_ED" #26
index_edad = "CH06" #13

def columna_universitario_numerica(file):
    """Agrega la columna de universitario al archivo de individuos"""
    # Abro el archivo para leer
    with open(file, newline='') as archivo: # No utilizo el encoding='utf-8' por el siguiente error UnicodeDecodeError: 'utf-8' codec can't decode byte 0xed in position 2457: invalid continuation byte
        csv_reader = csv.DictReader(archivo, delimiter=';')
        header = csv_reader.fieldnames + ['UNIVERSITARIO']
        filas = []  # Guardo las filas en una lista para ir agregando la nueva columna

        # Recorro el cuerpo del archivo y agrego la nueva columna
        for line in csv_reader:
            if int(line[index_edad]) >= 18 and int(line[index_nivelEd]) == 6:
                line["UNIVERSITARIO"] = 1  # Si es mayor de edad y completó la universidad
            elif int(line[index_edad]) >= 18 and int(line[index_nivelEd]) != 6:
                line["UNIVERSITARIO"] = 2  # Si es mayor de edad pero no completó la universidad
            else:
                line["UNIVERSITARIO"] = 0  # Si no tiene ninguna de las anteriores

            filas.append(line)  # Agrego la fila procesada a 'filas'

    # Escribo el archivo con la nueva columna
    with open(file, 'w', newline='') as archivo:
        csv_writer = csv.DictWriter(archivo,fieldnames=header, delimiter=';')
        csv_writer.writeheader()  # Escribo el header
        csv_writer.writerows(filas)  # Escribo las filas procesadas
