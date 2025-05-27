import csv
#EJERCICIO 12 SECCION B
# Constantes para nombres de columnas
index_anio = "ANO4"
index_trimestre = "TRIMESTRE"
index_condicion = "CONDICION_DE_HABITABILIDAD"
index_codUsu = "CODUSU"
index_nroHogar = "NRO_HOGAR"
index_actividad = "CONDICION_ACTIVIDAD"
index_aglomerado = "AGLOMERADO"
index_pondera = "PONDERA"

def porcentaje_jubilados_insuficiente(archivo_hogares, archivo_individuos):
    """Calcula el porcentaje de jubilados con viviendas insuficientes por aglomerado en el último trimestre"""

    # Determinar último año y trimestre
    trimestres_validos = []

    with open(archivo_individuos, newline="", encoding="utf-8") as individuos:
        reader = csv.DictReader(individuos, delimiter=";")
        for linea in reader:
            trimestres_validos.append((linea[index_anio], linea[index_trimestre]))

    # Encontrar el último trimestre por año
    ultimo_anio, ultimo_trimestre = max(trimestres_validos, key=lambda t: (int(t[0]), int(t[1])))

    # Guardar viviendas con habitabilidad insuficiente
    viviendas_insuficientes = set()

    with open(archivo_hogares, newline="", encoding="utf-8") as hogares:
        reader = csv.DictReader(hogares, delimiter=";")
        for linea in reader:
            if linea[index_anio] == ultimo_anio and linea[index_trimestre] == ultimo_trimestre:
                if linea[index_condicion] == "Insuficiente":
                    viviendas_insuficientes.add((linea[index_codUsu], linea[index_nroHogar]))

    # Contadores por aglomerado
    total_jubilados = {}
    jubilados_insuficientes = {}

    with open(archivo_individuos, newline="", encoding="utf-8") as individuos:
        reader = csv.DictReader(individuos, delimiter=";")
        for linea in reader:
            if linea[index_anio] == ultimo_anio and linea[index_trimestre] == ultimo_trimestre:
                if linea[index_actividad] == "Jubilado":
                    aglomerado = linea[index_aglomerado]
                    pondera = int(linea[index_pondera])

                    total_jubilados[aglomerado] = total_jubilados.get(aglomerado, 0) + pondera

                    if (linea[index_codUsu], linea[index_nroHogar]) in viviendas_insuficientes:
                        jubilados_insuficientes[aglomerado] = jubilados_insuficientes.get(aglomerado, 0) + pondera

    # Mostrar resultados
    print("Porcentaje de jubilados en viviendas con habitabilidad insuficiente por aglomerado:\n")
    for aglomerado in total_jubilados:
        total = total_jubilados[aglomerado]
        insuf = jubilados_insuficientes.get(aglomerado, 0)
        porcentaje = (insuf / total) * 100 if total > 0 else 0
        print(f"Aglomerado {aglomerado}: {porcentaje:.2f}%")
