from utils.rutas import data_path

def correspondencias():
    """Funcion que corrobora las correspondencias de los archivos individuos y hogares"""
    listaArchivosActuales = []
    for archivo in data_path.iterdir():
        listaArchivosActuales.append(archivo.name)
        
    for nombre in listaArchivosActuales:
        print(nombre)
    
    dicContador = {}
    for archivo in listaArchivosActuales:
        if archivo.startswith('usu'):
            partes = archivo.split("_")
            tipo = partes[1]  # 'hogar' o 'individual'
            codigo = partes[2].split(".")[0]

            if codigo not in dicContador:
                dicContador[codigo] = {"hogar": 0, "individual": 0}

            if "hogar" in tipo:
                dicContador[codigo]["hogar"] += 1
            elif "individual" in tipo:
                dicContador[codigo]["individual"] += 1

    listaResultante = []
    for clave, valor in dicContador.items():
        if valor["hogar"] == 0 or valor["individual"] == 0:
            listaResultante.append(clave)

    listaNombres = []
    for codigo in listaResultante:
        for archivo in listaArchivosActuales:
            if codigo in archivo:
                listaNombres.append(archivo)
    
    return listaNombres