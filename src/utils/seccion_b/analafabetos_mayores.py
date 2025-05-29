import pandas as pd
def mayoresA6(archivo):
    import csv
    import pandas as pd

    index_edad = "CH06"
    index_año = "ANO4"
    index_trimestre = "TRIMESTRE"
    index_leer_escribir = "CH09"
    index_pondera = "PONDERA"

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
                    continue

    data = []
    for año in sorted(dicTotales):
        total = dicTotales[año]
        porcentaje_no = (dicCumplen.get(año, 0) * 100) / total if total else 0
        porcentaje_si = (dicNoCumplen.get(año, 0) * 100) / total if total else 0
        data.append({
            "Año": año,
            "Saben leer y escribir (%)": round(porcentaje_si, 2),
            "No saben leer ni escribir (%)": round(porcentaje_no, 2)
        })

    return pd.DataFrame(data)
