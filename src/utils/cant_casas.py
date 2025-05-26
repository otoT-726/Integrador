def cant_casas(cuerpo):
    """Retorna la cantidad de casas del archivo csv"""
    cant = 0
    for renglon in cuerpo:
        cant += int(renglon[8])
    return cant