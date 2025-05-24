import csv

index_edad = "CH06"
index_año = "ANO4"
index_trimestre = "TRIMESTRE"
index_leer_escribir = "CH09"
index_pondera = "PONDERA"

def mayoresA6(archivo):
    """Función que calcula el porcentaje de personas mayores a 6 que no saben leer ni escribir en cada año en el último trimestre"""
    with open(archivo, encoding='utf-8') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        dicCumplen = {}
        dicTotales = {}
        dicNoCumplen = {}

        for line in csv_reader:
            if line[index_trimestre] == "3":
                try:
                    edad = int(line[index_edad])
                    leer_escribir = line[index_leer_escribir]
                    ponderacion = int(line[index_pondera])
                    año = line[index_año]

                    if edad > 6:
                        dicTotales[año] = dicTotales.get(año, 0) + ponderacion
                        if leer_escribir == "2":
                            dicCumplen[año] = dicCumplen.get(año, 0) + ponderacion
                        elif leer_escribir == "1":
                            dicNoCumplen[año] = dicNoCumplen.get(año, 0) + ponderacion
                except ValueError:
                    continue  # En caso de datos faltantes o mal formateados

    for año in dicTotales:
        try:
            
            porcentaje_no_saben = (dicCumplen.get(año, 0) * 100) / dicTotales[año]
            porcentaje_saben = (dicNoCumplen.get(año, 0) * 100) / dicTotales[año]
        except ZeroDivisionError:
            porcentaje_no_saben = 0
            porcentaje_saben = 0

        print(f'En el año {año} hubo un {porcentaje_no_saben:.2f}% de personas mayores de 6 que no saben leer ni escribir')
        print(f'En el año {año} hubo un {porcentaje_saben:.2f}% de personas mayores de 6 que saben leer y escribir')
