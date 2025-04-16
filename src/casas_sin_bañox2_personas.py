def casas_sin_baño(datos):
    dicc = {}
    for i in datos:
        aglomerado = int(i[7])
        dicc[aglomerado] = 0
    for renglon in datos:
        cant_habitantes = int(renglon[64]) #Cantidad habitantes por casa
        info_baños = int(renglon[41]) #Datos de la tenencia de baños
        aglomerado = int(renglon[7])
        pondera = int(renglon[8]) 
        if(cant_habitantes > 1 and info_baños == 4):
            dicc[aglomerado] += pondera
        for clave, valor in dicc.items():
            maxpos, minpos, max, min = 0, 0, 0, 9999
            if(valor > max):
                max = valor
                maxpos = clave
            elif(valor < min):
                min = valor
                minpos = clave
    print(dicc)
    print('La region con mas casas con dos habitantes y sin baños es: ', maxpos) #Es la 33, pero no se como poner la key buscando maximo value
    print('La region con menos casas con dos habitantes y sin baños es:', minpos) #lo mismo aca
