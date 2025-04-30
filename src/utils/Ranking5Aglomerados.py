import csv
INDEX_CANT_MIEMBROS = "IX_TOT" #
INDEX_NIVEL_ED = "NIVEL_ED" #
INDEX_AGLOMERADO = "AGLOMERADO" #
INDEX_PONDERACION = "PONDERA" #9
def rankin(individuos,hogar):
    with open(individuos,"r") as archivoInd:
        csv_reader = csv.DictReader(archivoInd, delimiter=";")
        # recorro el archivo de individuos y guardando en un diccionario el nivel educativo de cada codigo de usuario en una clave llamada "nivel"
        diccionarioIND = {}
        for line in csv_reader :
            cod = line["CODUSU"]
            diccionarioIND[cod] =  line[INDEX_NIVEL_ED]
        # diccionario cargado
    
    with open( hogar,"r") as archivoHogar:
        csv_reader = csv.DictReader(archivoHogar, delimiter=";")
        #print("columnas ", csv_reader.fieldnames)
    # me guarde en variables cuerpoIND y cuerpoHOG los archivos en modo csv para luego recorrerlos

        dicAglomerado = {} # diccionario para los que cumplen condicion
        dicTotal = {} # diccionario para los que cumplen/no cumplen condicion
        ListaPorcentaje = [] # lista con porcentaje de cada aglomeracion

        for line in csv_reader: #recorro el cuerpo de hogares
            usuarioActual = line["CODUSU"] # esto guarda el valor de la columna 0, que es el codigo de usuario
            Aglomerado = line[INDEX_AGLOMERADO]
            Pondera = float(line[INDEX_PONDERACION])
            Miembros = int(line[INDEX_CANT_MIEMBROS])

            if usuarioActual in diccionarioIND: # si el usuario de mi hogar se encuentra en el archivo tambien de individuos evaluo las condiciones
                nivelUsuario = diccionarioIND[usuarioActual]
                if (Miembros >= 2) and (nivelUsuario == "4" or nivelUsuario == "6"):
                    dicAglomerado[Aglomerado] = dicAglomerado.get(Aglomerado, 0) + Pondera
                    #esto lo que hace es verificar si existe o no la clave,de existir trae lo que ya tiene esa clave,sino pone 0 y acumula a raiz del 0
            dicTotal[Aglomerado] = dicTotal.get(Aglomerado, 0) + Pondera
                # lo mismo aca
        
        #al salir del for, me quedaron cargados los diccionarios cargados
        #dicAglomerado quedo con cada AGLOMERACION QUE CUMPLE  y todas sus ponderaciones
        #dicTotal quedo con cada AGLOMERACION QUE CUMPLE Y NO CUMPLE y todas sus ponderaciones

        for codigos in dicTotal.keys() : # voy a recorrer el diccionario de totales por claves
            if codigos in dicAglomerado: # busco el codigo del diccionario total, en el diccionario que cumplen
                porcentaje = ((dicAglomerado[codigos])/dicTotal[codigos] * 100) # el valor que guardare en mi lista de porcentajes
                ListaPorcentaje.append((codigos,porcentaje))

        #en rank5 queda almacenada una lista ordenada
        rank5 = sorted(ListaPorcentaje, key=lambda x:x[1],reverse=True)[:5]
                #ordena = la lista por clave, x: x[1] (es el porcentaje), de mayor a menor y los primeros 5
        print("RANKIN DE LOS 5 AGLOMERADOS QUE CUMPLEN")
        i = 1
        for aglo, porc in rank5:
            print(f"{i}°  : {aglo} con porcentaje de {porc:.2f} %")
            i+=1

                



