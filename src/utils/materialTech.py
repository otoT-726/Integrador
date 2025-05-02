import csv

indice_v4 = "IV4"
indice_ixtot = "IX_TOT"

def clasificar_material(v4):
    if v4 in ['1', '2', '3', '4']:
        return "Material durable"
    elif v4 in ['5', '6', '7']:
        return "Material precario"
    elif v4 == '9':
        return "No aplica"
    else:
        return "Valor desconocido"

def clasificar_densidad(IX_TOT):
    valor = float(IX_TOT)
    if valor < 1:
        return "Bajo"
    elif valor < 2:
        return "Medio"
    else:
        return "Alto"

def agregar_material_techumbre_y_densidad(ruta):
    """Lee el archivo CSV y agrega las columnas MATERIAL_TECHUMBRE y DENSIDAD_HOGAR"""
    with open(ruta, encoding="utf-8") as archivo:
        csv_reader = csv.DictReader(archivo, delimiter=";")
        header, datos = csv_reader.fieldnames + ["MATERIAL_TECHUMBRE", "DENSIDAD_HOGAR"], list(csv_reader)

    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        csv_writer = csv.DictWriter(archivo, fieldnames=header, delimiter=";")
        csv_writer.writeheader()

        for linea in datos:
            v4_valor = linea.get(indice_v4, "")
            ixtot_valor = linea.get(indice_ixtot, "0")

            linea["MATERIAL_TECHUMBRE"] = clasificar_material(v4_valor)
            linea["DENSIDAD_HOGAR"] = clasificar_densidad(ixtot_valor)

            csv_writer.writerow(linea)
