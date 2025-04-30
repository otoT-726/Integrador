import csv

index_nivelED= "NIVEL_ED"
index_anio = "ANO4"
index_trimestre = "TRIMESTRE"
index_condicion = "CONDICION_DE_HABITABILIDAD"
index_codUsu = "CODUSU"
index_nroHogar = "NRO_HOGAR"
index_pondera = "PONDERA"

def personas_universitario_insuficiente(archivo_hogares, archivo_individuos):
    anio = input("Ingresá el año a analizar: ")
    viviendas_insuficientes = set()
    cantidad = 0

    with open(archivo_hogares, newline="", encoding="utf-8") as hogares:
        """Recorre el archivo hogares y guarda las viviendas insuficientes"""
        hogares_reader = csv.DictReader(hogares, delimiter=";")
        for linea in hogares_reader:
            if linea[index_anio] == anio and linea[index_trimestre] == "3":
                if linea[index_condicion] == "Insuficiente":
                    viviendas_insuficientes.add((linea[index_codUsu], linea[index_nroHogar]))

    with open(archivo_individuos, newline="", encoding="utf-8") as individuos:
        """Recorre el archivo individuos y cuenta las personas universitarias insuficientes en las viviendas insuficientes con mismo codUsu y nroHogar"""
        individuos_reader = csv.DictReader(individuos, delimiter=";")
        for linea in individuos_reader:
            if linea[index_anio] == anio and linea[index_trimestre] == "3":
                if (linea[index_codUsu], linea[index_nroHogar]) in viviendas_insuficientes:
                    if linea[index_nivelED] == "3" or linea[index_nivelED] == "4" or linea[index_nivelED] == "5" or linea[index_nivelED] == "6":
                        cantidad += int(linea[index_pondera])

    print(cantidad)
