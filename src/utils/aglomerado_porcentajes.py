import csv
from pathlib import Path

index_aglomerado = "AGLOMERADO"
index_condicion = "CONDICION_DE_HABITABILIDAD"
index_trimestre = "TRIMESTRE"

aglomeradosCump = {}
aglomeradosTot = {}

aglomerados = {
    "Gran La Plata": 0,
    "Bahía Blanca - Cerri": 0,
    "Gran Rosario" : 0,
    "Gran Santa Fé": 0,
    "Gran Paraná": 0,
    "Posadas": 0,
    "Gran Resistencia": 0,
    "Comodoro Rivadavia - Rada Tilly": 0,
    "Gran Mendoza": 0,
    "Corrientes": 0,
    "Gran Córdoba": 0,
    "Concordia": 0,
    "Formosa": 0,
    "Neuquén – Plottier": 0,
    "Santiago del Estero - La Banda": 0,
    "Jujuy - Palpalá": 0,
    "Río Gallegos": 0,
    "Gran Catamarca": 0,
    "Gran Salta": 0,
    "La Rioja": 0,
    "Gran San Luis": 0,
    "Gran San Juan": 0,
    "Gran Tucumán - Tafí Viejo": 0,
    "Santa Rosa – Toay": 0,
    "Ushuaia - Río Grande": 0,
    "Ciudad Autónoma de Buenos Aires": 0,
    "Partidos del GBA": 0,
    "Mar del Plata": 0,
    "Río Cuarto": 0,
    "San Nicolás – Villa Constitución": 0,
    "Rawson – Trelew": 0,
    "Viedma – Carmen de Patagones": 0
}

codigo_a_nombre = {
    "2": "Gran La Plata",
    "3": "Gran Córdoba",
    "4": "Gran Rosario",
    "5": "Gran Santa Fé",
    "6": "Gran Mendoza",
    "7": "Gran San Juan",
    "8": "Gran Salta",
    "9": "Gran Tucumán - Tafí Viejo",
    "10": "Gran Paraná",
    "11": "Posadas",
    "12": "Gran Resistencia",
    "13": "Corrientes",
    "14": "Formosa",
    "15": "Santiago del Estero - La Banda",
    "16": "Santa Rosa – Toay",
    "17": "Río Cuarto",
    "18": "San Nicolás – Villa Constitución",
    "19": "Rawson – Trelew",
    "20": "Viedma – Carmen de Patagones",
    "21": "Gran Catamarca",
    "22": "La Rioja",
    "23": "Gran San Luis",
    "24": "Bahía Blanca - Cerri",
    "25": "Mar del Plata",
    "26": "Comodoro Rivadavia - Rada Tilly",
    "27": "Neuquén – Plottier",
    "28": "Río Gallegos",
    "29": "Ushuaia - Río Grande",
    "30": "Ciudad Autónoma de Buenos Aires",
    "31": "Partidos del GBA",
    "32": "Concordia",
    "33": "Jujuy - Palpalá"
}

def procentajeAglomerado(archivo_hogares):
    with open(archivo_hogares, newline="", encoding="utf-8") as archivo:
        csv_reader = csv.DictReader(archivo, delimiter=";")
        
        for linea in csv_reader:
            ponderacion = int(linea["PONDERA"])
            cumplen = 0
            total = 0
            if linea[index_trimestre] == "3":
                nombre_aglomerado = codigo_a_nombre.get(linea[index_aglomerado].strip())
                if nombre_aglomerado in aglomerados.keys():
                    if linea[index_condicion].strip().lower() == "insuficiente":
                        cumplen = ponderacion
                    total += ponderacion
                    
                    aglomeradosCump[nombre_aglomerado] = aglomeradosCump.get(nombre_aglomerado, 0) + cumplen
                    aglomeradosTot[nombre_aglomerado] = aglomeradosTot.get(nombre_aglomerado, 0) + total
        for llave in aglomeradosCump.keys():
            prom = aglomeradosCump[llave] * 100 / aglomeradosTot[llave]
            aglomerados[llave] = prom
        for aglom in aglomerados:
            print(f'{aglom}: {round(aglomerados[aglom], 2)}%') 

