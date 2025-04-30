import csv

index_aglomerado = "AGLOMERADO"
index_ch06 = "CH06"
index_nivel = "NIVEL_ED"
index_anio = "ANO4"
index_trimestre = "TRIMESTRE"

#recibo una lista de sublistas con la informacion filtrada por aglomeracion ingresada y por mayores de edad
def crearDiccionario(archivo):
    dicAglomerado = {}

    tipos = [
        "Primario Incompleto",  # nivel 1
        "Primario Incompleto",  # nivel 2
        "Secundario Incompleto",  # nivel 3
        "Secundario Completo",  # nivel 4
        "Superior o Universitario"  # nivel 5
    ]

    for fila in archivo:
        anio = fila[index_anio]
        trimestre = fila[index_trimestre]

        try:
            nivel = int(fila[index_nivel])
        except:
            continue  # salta si no es número
        if nivel < 1 or nivel > 5:
            continue  # fuera del rango esperado
        tipo_nivel = tipos[nivel - 1]
        if anio not in dicAglomerado:
            dicAglomerado[anio] = {}
        if trimestre not in dicAglomerado[anio]:
            dicAglomerado[anio][trimestre] = {}
        if tipo_nivel not in dicAglomerado[anio][trimestre]:
            dicAglomerado[anio][trimestre][tipo_nivel] = 1
        else:
            dicAglomerado[anio][trimestre][tipo_nivel] += 1
    print("Se creó el diccionario con la información de años, trimestres y niveles")
    return dicAglomerado
                    
def filtrar_info(archivo, numero_aglomerado):
    data_filtrada = []
    csv_reader = csv.DictReader(archivo, delimiter=";")
    for fila in csv_reader:
        try:
            aglomerado = int(fila[index_aglomerado])
            ch06 = int(fila[index_ch06])
            if (aglomerado == int(numero_aglomerado) and ch06 >= 18):
                data_filtrada.append(fila)
        except:
            continue  # Ignorar filas inválidas
    print("Se filtro la informacion del archivo csv")
    #data_filtrada es una lista de diccionarios, cada diccionario tiene la info de una fila del csv
    return crearDiccionario(data_filtrada)


def crearTabla(archivo_individuos):
    aglomerado = input("ingrese un numero de aglomerado ")
    with open(archivo_individuos,encoding="utf-8") as arch:
        informacion = filtrar_info(arch, aglomerado)
        print("IMPRIMO INFORMAACION DEL DICCIONARIO")
        print("-"*50)
        #voy a tomar del diccionario de años,el diccionario de trimestres
    for anio,trimestres in informacion.items():
        print(f"Año: {anio}")
        for trim, nivel in trimestres.items():
            print(f"    Trimestre: {trim}")
            for clave,valor in nivel.items() :
                print(f"Nivel {clave} : {valor}")
