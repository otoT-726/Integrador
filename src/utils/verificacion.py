from src.utils.rutas import data_path
def correspondencias():
    """Funcion que corrobora las correspondencias de los archivos individuos y hogares"""
    listaArchivosActuales = []
    for archivo in data_path.iterdir():
        listaArchivosActuales.append(archivo.name)
        
    for nombre in listaArchivosActuales:
        print(nombre)
    
    dicContador = {}
    for archivo in listaArchivosActuales:
        
        #Necesito agarrar los codigos de los archivos
        if(archivo.startswith('usu')):
            codigo = archivo.split("_")[2].split(".")[0]
                    
            if(codigo not in dicContador):
                dicContador[codigo] = 1
            else:
                dicContador[codigo] += 1
            
    listaResultante = []
    
    for clave,valor in dicContador.items():
        if(valor == 1):
            listaResultante.append(clave)

    listaNombres = []
    for codigo in listaResultante:
        for archivo in listaArchivosActuales:
            if(codigo in archivo):
                listaNombres.append(archivo)
    
    return listaNombres