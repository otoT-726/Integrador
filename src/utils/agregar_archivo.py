import csv

def agregar_trimestre(maestro, detalle):
    """Agrega los datos de un trimestre de eph a nuestra base de datos"""
    with open(detalle, newline="") as archivo:
        csv_reader = csv.reader(archivo, delimiter= ";")
        salteo= next(csv_reader)
        with open(maestro, "a", newline= "") as archivo:
            csv_writer = csv.writer(archivo, delimiter=";")
            for line in csv_reader:
                csv_writer.writerow(line)