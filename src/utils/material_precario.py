import csv 
""""
1. Abrir el archivo CSV (el txt separado por ";").
2. Buscar filas del año ingresado.
3. De esas filas, encontrar el último trimestre.
4. Trabajar solo con esas filas.
5. Para cada aglomerado:
    - Contar cuántas viviendas totales hay.
    - Contar cuántas son de material precario.
6. Calcular porcentaje = (precarias / total) * 100.
7. Buscar:
    - El aglomerado con mayor porcentaje.
    - El aglomerado con menor porcentaje.
8. Mostrar los resultados.
"""

def material_precario(año, archivo):
    """ Informa el aglomerado con mayor y menor porcentaje de viviendas de material precario en el último trimestre del año. """

    index_año = "ANO4"
    index_trimestre = "TRIMESTRE"
    index_material_techumbre = "MATERIAL_TECHUMBRE"
    index_aglomerado = "AGLOMERADO"
    index_pondera = "PONDERA" #pondera es la cantidad de viviendas que tiene cada aglomerado

    trimestres_maximo = -1 #guardar el trimestre maximo
    datos_filtrados = [] #lista para guardar los datos filtrados

    # Primero buscamos los trimestres disponibles del año elegido
    with open(archivo,encoding="utf-8") as file:
        csv_reader = csv.DictReader(file, delimiter=";")
        next(csv_reader)

        for line in csv_reader:
            # Obtener el último trimestre del año seleccionado
            año_archivo = line[index_año]
            trimestre = int(line[index_trimestre])
            #filtro por año y trimestre
            if (año_archivo ==año):
                if (trimestre > trimestres_maximo):
                    trimestres_maximo = trimestre
                    datos_filtrados = [line]#resetear la lista con esta nueva fila  
                elif (trimestre == trimestres_maximo):
                    datos_filtrados.append(line)# si es el mismo solo acumulo datos en mi lista 

                
    # paso 2 Acumular datos por aglomerado (ahora `datos_filtrados` ya contiene las filas del último trimestre)
    datos_aglomeradoTotal = {}
    datos_aglomeradoCondicion = {}	
    for line in datos_filtrados:#recorodo la lista de datos filtrados
        aglomerado = int(line[index_aglomerado])
        material = line[index_material_techumbre]
        pondera = int(line[index_pondera])

        if aglomerado not in datos_aglomeradoTotal:
            datos_aglomeradoTotal[aglomerado] = 0
            datos_aglomeradoCondicion[aglomerado] = 0
        #acumulo el pondera para el total de viviendas
        datos_aglomeradoTotal[aglomerado] += pondera
        # si es material precario acumulo en el otro indice
        if material == "Material precario":
            datos_aglomeradoCondicion[aglomerado] += pondera
        #'Aglomerado 1': {'total': 1200, 'precarios': 300},

    #paso 3 calculo el porcentaje de viviendas precarias por aglomerado
    porcentajes = {}
    #'Aglomerado 1': 12.5,
    #'Aglomerado 2': 8.3,
    #'Aglomerado 3': 5.0,
    #'Aglomerado 4': 20.7



    for aglomerado in datos_aglomeradoTotal.keys():
        try:
            porcentaje = (datos_aglomeradoCondicion[aglomerado]  * 100)/ datos_aglomeradoTotal[aglomerado]
            porcentajes[aglomerado] = porcentaje
        except ZeroDivisionError:
                # Esto no debería ocurrir gracias a la validación anterior, pero es una medida extra
                print(f"Error al calcular el porcentaje para el aglomerado {aglomerado} debido a un total 0.")

    # paso 4 buscar el aglomerado con mayor y menor porcentaje
    for localidad,valor in porcentajes.items():
        print(f'En el aglomerado {localidad} hay un {valor:.2f}% de viviendas de material precario.')
    
    aglo_max = {}
    aglo_min = {}

    aglo_max =  max(porcentajes.items(), key=lambda x : x[1]) # el items de un diccionario devuelve la clave y el valor en una tupla
    aglo_min = min(porcentajes.items(), key=lambda x : x[1])

    print(aglo_max)
    print(aglo_min)


    """print(f'El aglomerado maximo es {aglo_max[]} con un {aglo_max[1]}% de viviendas de material precario.')
    print(f'El aglomerado minimo es {aglo_min[0]} con un {aglo_min[1]}% de viviendas de material precario.')"""



def obtener_anos(archivo):
    """Extrae los años únicos del archivo"""
    index_año = "ANO4"
    anos = set()  # Usamos un set para evitar duplicados
    with open(archivo,encoding="utf-8") as file:
        csv_reader = csv.DictReader(file, delimiter=";")
        next(csv_reader)  # Saltamos la primera fila (encabezado)

        # Recorremos el archivo y extraemos los años 
        for line in csv_reader:
            año = line[index_año]  
            anos.add(año)

    return sorted(anos)  # Devolvemos la lista de años 